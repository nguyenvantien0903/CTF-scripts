import java.util.Random;
import java.util.Scanner;

public class CrackMe {
    public static void main(String[] arrstring) {
        int n;
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is the flag?");
        String string = scanner.nextLine();
        if (string.length() != 22) {
            System.out.println("Not the flag :(");
            return;
        }
        char[] arrc = new char[string.length()];
        for (n = 0; n < string.length(); ++n) {
            arrc[n] = string.charAt(n);
        }
        for (n = 0; n < string.length() / 2; ++n) {
            char c = arrc[string.length() - n - 1];
            arrc[string.length() - n - 1] = arrc[n];
            arrc[n] = c;
        }
        int[] arrn = new int[]{19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1};
        int[] arrn2 = new int[arrc.length];
        for (int i = arrn.length - 1; i >= 0; --i) {
            arrn2[i] = arrc[arrn[i]];
        }
        Random random = new Random();
        random.setSeed(431289L);
        int[] arrn3 = new int[string.length()];
        for (int i = 0; i < string.length(); ++i) {
            arrn3[i] = arrn2[i] ^ random.nextInt(i + 1);

        }
        Object object = "";
        for (int i = 0; i < arrn3.length; ++i) {
            object = (String)object + arrn3[i] + ".";
        }
        System.out.println("\nYOUR FLAG: " + (String)object);
        if (((String)object).equals("116.122.54.50.93.66.98.117.75.51.97.78.104.119.90.53.94.36.105.84.40.69.")) {
            System.out.println("Congrats! You got the flag!");
        } else {
            System.out.println("Not the flag :(");
        }




        Random var133 = new Random();
         var133.setSeed(431289L);
         System.out.println("rev2");
         int[] res = new int[]{116,122,54,50,93,66,98,117,75,51,97,78,104,119,90,53,94,36,105,84,40,69};
         for(int i = 0; i < string.length(); ++i) {
            System.out.print((char)res[i]);
         }
         System.out.println("");
         for(int k = 0; k < string.length(); ++k) {
            res[k] = res[k] ^ var133.nextInt(k + 1);
            System.out.println(var133.nextInt(k + 1));
         }
         for(int i = 0; i < string.length(); ++i) {
            System.out.print((char)res[i]);
         }
         System.out.println("");

         int[] aaa = new int[string.length()];
         for(int j = string.length() - 1; j >= 0; --j) {
            aaa[arrn[j]] = res[j];
         }
         for(int i = 0; i < string.length(); ++i) {
            System.out.print((char)aaa[i]);
         }
         System.out.println("");
    }
}