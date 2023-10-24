import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int count = 0;


        if (n == 3)
            count = 1;

        if (n == 4)
            count = -1;

        if (n % 5 == 0) {
            count = n / 5;
        } else {

            for (int i = 1; i < (n / 3); i++)
                if ((n - (3 * i)) % 5 == 0) {

                    int fiveCount = (n - 3 * i) / 5;

                    count = i + fiveCount;

                    break;

                } else if (n % 3 == 0) {
                    count = n / 3;

                } else
                    count = -1;
        }
        System.out.println(count);
    }
}