#!/usr/bin/env python3
"""Simulador de quitação de dívidas: avalanche x bola de neve.

Uso:
    python3 quitacao.py dividas.json
    python3 quitacao.py dividas.json --estrategia avalanche

Formato do JSON (valores em reais, juros em % ao mês):
{
  "extra_mensal": 1500,
  "dividas": [
    {"nome": "Fatura parcelada", "saldo": 3000, "juros_am": 9, "parcela_minima": 400}
  ]
}

"extra_mensal" é o dinheiro que sobra ALÉM das parcelas mínimas. Quando uma
dívida acaba, a parcela dela vira extra para a próxima (efeito bola de neve).
Só usa a biblioteca padrão. É simulação com juros constantes, não promessa:
juros reais mudam e o contrato manda.
"""
import argparse
import json
import sys

MAX_MESES = 600


def simular(dados, estrategia):
    dividas = [
        {"nome": d["nome"], "saldo": float(d["saldo"]),
         "i": float(d["juros_am"]) / 100.0, "min": float(d["parcela_minima"]),
         "quitada_em": None}
        for d in dados["dividas"]
    ]
    extra = float(dados.get("extra_mensal", 0))
    total_juros = 0.0
    total_pago = 0.0

    def chave(d):
        # avalanche: maior juros primeiro; bola de neve: menor saldo primeiro
        return (-d["i"], d["saldo"]) if estrategia == "avalanche" else (d["saldo"], -d["i"])

    for mes in range(1, MAX_MESES + 1):
        abertas = [d for d in dividas if d["saldo"] > 0.005]
        if not abertas:
            break
        # 1) juros do mês
        for d in abertas:
            j = d["saldo"] * d["i"]
            d["saldo"] += j
            total_juros += j
        # 2) mínimos
        liberado = extra
        for d in abertas:
            pg = min(d["min"], d["saldo"])
            d["saldo"] -= pg
            total_pago += pg
            if d["saldo"] <= 0.005:
                d["saldo"] = 0.0
                d["quitada_em"] = mes
                liberado += d["min"] - pg  # sobra do mínimo nesse mês
        # parcelas de dívidas já quitadas em meses anteriores rolam para o extra
        for d in dividas:
            if d["quitada_em"] is not None and d["quitada_em"] < mes:
                liberado += d["min"]
        # 3) extra na dívida prioritária
        for d in sorted([x for x in dividas if x["saldo"] > 0.005], key=chave):
            if liberado <= 0:
                break
            pg = min(liberado, d["saldo"])
            d["saldo"] -= pg
            total_pago += pg
            liberado -= pg
            if d["saldo"] <= 0.005:
                d["saldo"] = 0.0
                d["quitada_em"] = mes
    else:
        return None  # não quita em MAX_MESES

    meses = max(d["quitada_em"] for d in dividas)
    return {"meses": meses, "juros": total_juros, "pago": total_pago,
            "ordem": sorted(dividas, key=lambda d: d["quitada_em"])}


def brl(v):
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("--estrategia", choices=["avalanche", "bola-de-neve", "ambas"], default="ambas")
    a = ap.parse_args()

    with open(a.arquivo, encoding="utf-8") as f:
        dados = json.load(f)

    # aviso de armadilha: mínimo que não cobre os juros
    for d in dados["dividas"]:
        juros = float(d["saldo"]) * float(d["juros_am"]) / 100
        if float(d["parcela_minima"]) <= juros:
            print(f"ATENÇÃO: '{d['nome']}' tem parcela mínima ({brl(float(d['parcela_minima']))}) "
                  f"menor ou igual aos juros do mês ({brl(juros)}). Sem extra, o saldo não cai.")

    total = sum(float(d["saldo"]) for d in dados["dividas"])
    juros_mes = sum(float(d["saldo"]) * float(d["juros_am"]) / 100 for d in dados["dividas"])
    print(f"Total devido: {brl(total)} | juros só neste mês: {brl(juros_mes)} | extra mensal: {brl(float(dados.get('extra_mensal', 0)))}\n")

    estrategias = ["avalanche", "bola-de-neve"] if a.estrategia == "ambas" else [a.estrategia]
    res = {}
    for e in estrategias:
        r = simular(dados, "avalanche" if e == "avalanche" else "bola")
        res[e] = r
        print(f"== {e} ==")
        if r is None:
            print(f"Não quita em {MAX_MESES} meses com esses números. Revise extra, parcelas ou renegocie.\n")
            continue
        print(f"Quita tudo em {r['meses']} meses | juros totais: {brl(r['juros'])} | total pago: {brl(r['pago'])}")
        for d in r["ordem"]:
            print(f"  mês {d['quitada_em']:>3}: {d['nome']}")
        print()
    if len(res) == 2 and all(res.values()):
        dif = res["bola-de-neve"]["juros"] - res["avalanche"]["juros"]
        print(f"Diferença de juros (bola de neve - avalanche): {brl(dif)}")
        print("Se a diferença for pequena, escolha a que mantém você motivado.")


if __name__ == "__main__":
    sys.exit(main())
