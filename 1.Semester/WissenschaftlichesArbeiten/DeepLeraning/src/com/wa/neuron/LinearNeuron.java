package com.wa.neuron;

import java.util.ArrayList;

public class LinearNeuron {

	private double[] weigthList = new double[3];

	public LinearNeuron() {
		for (int i = 0; i < weigthList.length; i++) {
			weigthList[i] = Math.random();
		}
	}

	public double think(double[] aInput) {

		return sigmoid(aInput);
	}

	public void train(ArrayList<double[]> aTestDataInput, double[] aTestDataResult, int aAnzIteration) {

		for (int i = 0; i < aAnzIteration; i++) {
			int k = 0;
			for (double[] dTestValue : aTestDataInput) {
				// Thinking --> evaluete the sigmod value
				double hExpectetOutput = think(dTestValue);

				int j = 0;

				for (double d : dTestValue) {
					// Error --> get the errer value
					double hError = evaluateError(hExpectetOutput, aTestDataResult[k]);
					// Adjustment --> get the value for the adjustment of the weights
					double adjustValue = evaluteAdjustment(hError, d, sigmodDeraktiv(hExpectetOutput));

					weigthList[j] = weigthList[j] + adjustValue;

					j++;
				}
				k++;
			}
		}
	}

	private double evaluteAdjustment(double hError, double aTestDataInput, double sigmodDeraktiv) {

		return hError * aTestDataInput * sigmodDeraktiv;
	}

	private double sigmodDeraktiv(double hExpectetOutput) {

		return hExpectetOutput * (1 - hExpectetOutput);
	}

	private double evaluateError(double hExpectetOutput, double aTestDataResult) {

		return aTestDataResult - hExpectetOutput;
	}

	private double sigmoid(double[] aInputValue) {

		double hExpValue = 0.0;

		for (int i = 0; i < aInputValue.length; i++) {

			hExpValue = hExpValue + (aInputValue[i] * weigthList[i]);
		}

		return 1 / (1 + Math.exp(-hExpValue));
	}

	public void printWeigths() {
		System.out.println(String.format("[%f,%f,%f]", weigthList[0], weigthList[1], weigthList[2]));
	}
}
