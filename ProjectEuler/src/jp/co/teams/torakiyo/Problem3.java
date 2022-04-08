package jp.co.teams.torakiyo;

import java.util.ArrayList;
import java.util.List;

/********************************************
 * 13195 の素因数は 5, 7, 13, 29 である.
 * 600851475143 の素因数のうち最大のものを求めよ.
 ********************************************/

public class Problem3 {
	public static void main(String[] args) {

		long n = 600851475143L;

		List<Long> pfactors = new ArrayList<Long>();

		for (long i = 2; i <= n; i++) {

			while (n % i == 0) {
				pfactors.add(i);

				n = n / i;
			}
		}
		System.out.print(pfactors.get(pfactors.size() - 1));
	}
}