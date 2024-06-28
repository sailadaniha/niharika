public class IncrementDecrementTriangle {
    public static void main(String[] args) {
        int rows = 10;
         char startChar = 'A';
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= rows - i; j++) {
                System.out.print("  "); 
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(j + " ");
            }
            for (int j = i - 1; j >= 1; j--) {
                char ch = (char) (startChar + j - 1);
                System.out.print(ch + " ");
            }
            System.out.println();
        }
    }
}
