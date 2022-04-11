package jp.co.teams.torakiyo;

import java.util.ArrayList;
import java.util.List;

/*****************************************************************
 * 左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である. では,
 * 3桁の数の積で表される回文数の最大値を求めよ.
 *****************************************************************/

public class Problem4 {
	public static void main(String[] args) {
		for (int i = 100; i < 1000; i++) {
			for (int j = 100; j < 1000; j++) {
				List<Character> numList = new ArrayList<Character>();
				int reslutNum = j * i;

				for (char c : String.valueOf(reslutNum).toCharArray()) {
					numList.add(c);
				}
				int listLength = numList.size();
				if (numList.size() == 6 && numList.get(0).equals('9')
						&& numList.get(0).equals(numList.get(listLength - 1))
						&& numList.get(1).equals(numList.get(listLength - 2))
						&& numList.get(2).equals(numList.get(listLength - 3))) {
					System.out.println(reslutNum);
				}
			}
		}
	}

}
