public class ArrayFind {
        public static boolean check(Object[] a, Object x) {
            for (int i = 0; i < a.length; i++){
                if (x == a[i]){
                  return true;
                  }
              }
            return false;
        }
}
