package com.wa.main;

import java.util.ArrayList;
import java.io.IOException;
import java.util.*;

import com.wa.neuron.LinearNeuron;

public class DeepLearning {

	public static void main(String[] args) {
		LinearNeuron hLinearNeuron = new LinearNeuron();

		ArrayList<double[]> hTestData = new ArrayList<double[]>();
		hTestData.add(new double[] { 0.0, 0.0, 1.0 });
		hTestData.add(new double[] { 1.0, 1.0, 1.0 });
		hTestData.add(new double[] { 1.0, 0.0, 1.0 });
		hTestData.add(new double[] { 0.0, 1.0, 1.0 });

		double[] hErgData = new double[] { 0.0, 1.0, 1.0, 0.0 };

		hLinearNeuron.train(hTestData, hErgData, 100000);
		
		double hDbl = 0;
		Scanner src = new Scanner(System.in);
		int hIdx = 0;
		while (hIdx == 0) {

			try {
				Runtime.getRuntime().exec("clear");
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			if(hDbl != 0) {
				System.out.println(hDbl);
			}
			
			System.out.println("Please enter your values");
			
			double[] hTestArray = new double[3];

			for (int i = 0; i < 3; i++) {
				
				if (src.hasNextDouble()) {
					hTestArray[i] = src.nextDouble();
				} else {
					System.out.println("Shutting down ......");
					hIdx = 1;
					break;
				}
			}

			hDbl = hLinearNeuron.think(hTestArray);
		}
		src.close();
	}
}
