package com.lista02;

import java.util.Arrays;

public class AdalineNOR {
    private double[] pesos;
    private double taxaAprendizado;
    private double limiteAtivacao;

    public AdalineNOR(int numEntradas, double taxaAprendizado, double limiteAtivacao) {
        this.pesos = new double[numEntradas + 1]; // +1 para o peso do viés
        this.taxaAprendizado = taxaAprendizado;
        this.limiteAtivacao = limiteAtivacao;
        inicializarPesos();
    }

    private void inicializarPesos() {
        for (int i = 0; i < pesos.length; i++) {
            pesos[i] = Math.random() * 2 - 1; // inicialização aleatória entre -1 e 1
        }
    }

    private double funcaoAtivacao(double soma) {
        return (soma >= limiteAtivacao) ? 1 : 0;
    }

    public int calcularSaida(double[] entradas) {
        double soma = pesos[0]; // bias
        for (int i = 0; i < entradas.length; i++) {
            soma += entradas[i] * pesos[i + 1]; // pesos[i+1] corresponde aos pesos das entradas
        }
        return (int) funcaoAtivacao(soma);
    }

    public void treinar(double[][] entradas, int[] saidasEsperadas, int numEpocas) {
        for (int epoca = 0; epoca < numEpocas; epoca++) {
            for (int i = 0; i < entradas.length; i++) {
                double[] entrada = entradas[i];
                int saidaCalculada = calcularSaida(entrada);
                int erro = saidasEsperadas[i] - saidaCalculada;
                pesos[0] += taxaAprendizado * erro; // atualização do peso do viés

                for (int j = 0; j < entrada.length; j++) {
                    pesos[j + 1] += taxaAprendizado * erro * entrada[j]; // atualização dos pesos das entradas
                }
            }
        }
    }

    public static void main(String[] args) {
        int numEntradas = 3;
        double taxaAprendizado = 0.1;
        double limiteAtivacao = 0.5;
        int numEpocas = 1000;

        AdalineNOR adaline = new AdalineNOR(numEntradas, taxaAprendizado, limiteAtivacao);

        double[][] entradas = {
                { 0, 0, 0 },
                { 0, 0, 1 },
                { 0, 1, 0 },
                { 0, 1, 1 },
                { 1, 0, 0 },
                { 1, 0, 1 },
                { 1, 1, 0 },
                { 1, 1, 1 }
        };

        int[] saidasEsperadas = { 1, 0, 0, 0, 0, 0, 0, 0 }; // NOR

        adaline.treinar(entradas, saidasEsperadas, numEpocas);

        System.out.println("Pesos finais: " + Arrays.toString(adaline.pesos));

        // Testar a rede após o treinamento
        for (int i = 0; i < entradas.length; i++) {
            int saidaCalculada = adaline.calcularSaida(entradas[i]);
            System.out.println("Entrada: " + Arrays.toString(entradas[i]) + " Saida Calculada: " + saidaCalculada);
        }
    }
}
