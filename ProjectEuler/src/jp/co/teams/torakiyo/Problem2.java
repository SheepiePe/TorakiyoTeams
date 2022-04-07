package jp.co.teams.torakiyo;

public class Problem2 {

	/**************************************************************************************************
	 * フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである. 1, 2, 3, 5, 8, 13,
	 * 21, 34, 55, 89, ... 数列の項の値が400万以下のとき, 値が偶数の項の総和を求めよ.
	 * Note:お使いのパラメータが正しいかどうか確認してください.
	 **************************************************************************************************/

	public static void main(String[] args) {
		int sumCount = 0;
		int beforeNum = 0;
		int afterNum = 2;
		for (int i = 1; i < 4000000;) {
			beforeNum = i;
			if (i % 2 == 0) {
				sumCount += i;
			}
			if (i < 3) {
				i++;
			} else {
				i = i + afterNum;
			}
			afterNum = beforeNum;
		}
		System.out.println(sumCount);
	}

}
