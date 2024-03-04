package com.app;

import java.util.Random;

public class Perceptron {
    public static void main(String[] args) {
        int[][] trainingset = {{0,0,1}, {0,1,1}, {1,0,1}, {1,1,0}}; // portaNAND
        double eta = 0.1; // passo de aprendizado
        int maxiterations = 100;
        Random random = new Random();
        double w1 = random.nextDouble() * 0.4 - 0.2;
        double w2 = random.nextDouble() * 0.4 - 0.2;
        double w0 = 1;

        double error = random.nextDouble() * 0.4 - 0.2;
        int count = 0;
        while (count < maxiterations && error != 0) {
            error = 0;
            for (int[] array : trainingset) {
                int target = array[2];
                int output = 0;
                double summation = w1 * array[0] + w2 * array[1] - w0;
                if (summation <=0) {
                    output = 1;
                }

                if (output != target) {
                    error += 1;
                }

                w1 += eta * (target - output) * array[0]; // regra delta
                w2 += eta * (target - output) * array[1];
                w0 += eta * (target - output);

                System.out.println("Saída " + output + " target " + target);
                System.out.println("Erro " + error);
            }
            count++;
        }
        System.out.println("Iterações: " + count);
        System.out.println("Erro final: " + error);
        System.out.println("w1: " + w1 + ", w2: " + w2 + ", w0: " + w0);
    }
}
