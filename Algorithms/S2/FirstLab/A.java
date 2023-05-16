import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class A {
    public static class SegmentTree {
        private int[] tree;
        private int[] a;
        private int n;

        public SegmentTree(int[] a) {
            this.a = a;
            n = a.length;
            tree = new int[4 * n];
            build(1, 0, n - 1);
        }

        private void build(int v, int tl, int tr) {
            if (tl == tr) {
                tree[v] = a[tl];
            } else {
                int tm = (tl + tr) / 2;
                build(v * 2, tl, tm);
                build(v * 2 + 1, tm + 1, tr);
                tree[v] = Math.min(tree[v * 2], tree[v * 2 + 1]);
            }
        }

        public void set(int pos, int newVal) {
            set(1, 0, n - 1, pos, newVal);
        }

        private void set(int v, int tl, int tr, int pos, int newVal) {
            if (tl == tr) {
                tree[v] = newVal;
            } else {
                int tm = (tl + tr) / 2;
                if (pos <= tm) {
                    set(v * 2, tl, tm, pos, newVal);
                } else {
                    set(v * 2 + 1, tm + 1, tr, pos, newVal);
                }
                tree[v] = Math.min(tree[v * 2], tree[v * 2 + 1]);
            }
        }
        public int getMin(int l, int r) {
            return getMin(1, 0, n - 1, l, r);
        }

        private int getMin(int v, int tl, int tr, int l, int r) {
            if (l > r) {
                return Integer.MAX_VALUE;
            }
            if (l == tl && r == tr) {
                return tree[v];
            }
            int tm = (tl + tr) / 2;
            return Math.min(getMin(v * 2, tl, tm, l, Math.min(r, tm)),
                    getMin(v * 2 + 1, tm + 1, tr, Math.max(l, tm + 1), r));
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int[] a = new int[n];
        tokenizer = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(tokenizer.nextToken());
        }
        // Read from stdin "min 2 5"
        // Print to stdout "3"
        SegmentTree tree = new SegmentTree(a);
        tokenizer = new StringTokenizer(reader.readLine());
        while (tokenizer.hasMoreTokens()) {
            String command = tokenizer.nextToken();
            if (command.equals("min")) {
                int l = Integer.parseInt(tokenizer.nextToken());
                int r = Integer.parseInt(tokenizer.nextToken());
                System.out.println(tree.getMin(l, r));
            } else if (command.equals("set")) {
                int pos = Integer.parseInt(tokenizer.nextToken());
                int newVal = Integer.parseInt(tokenizer.nextToken());
                tree.set(pos, newVal);
            }
        }

    }
}
