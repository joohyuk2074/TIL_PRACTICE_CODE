package me.joohyuk.chapter11;

import java.util.Arrays;

public class Test1<K, V> {

    private static final int DEFAULT_CAPACITY = 16;
    private int size;

    @SuppressWarnings("unchecked")
    private MyEntry<K, V>[] entries = new MyEntry[DEFAULT_CAPACITY];

    public void put(K key, V value) {
        boolean success = true;

        for (int i = 0; i < size; i++) {
            if (entries[i].getKey().equals(key)) {
                entries[i].setValue(value);
                success = false;
            }
        }

        if (success) {
            checkCapacity();
            entries[size++] = new MyEntry<>(key, value);
        }
    }

    private void checkCapacity() {
        if (size == entries.length) {
            int newSize = entries.length * 2;
            entries = Arrays.copyOf(entries, newSize);
        }
    }

    public V get(K key) {
        for (int i = 0; i < size; i++) {
            if (entries[i] != null) {
                if (entries[i].getKey().equals(key)) {
                    return entries[i].getValue();
                }
            }
        }

        return null;
    }

    public void remove(K key) {
        for (int i = 0; i < size; i++) {
            if (entries[i].getValue().equals(key)) {
                entries[i] = null;
                size--;
                condenseArray(i);
            }
        }
    }

    private void condenseArray(int start) {
        int i;
        for (i = start; i < size; i++) {
            entries[i] = entries[i + 1];
        }

        entries[i] = null;
    }

    private final class MyEntry<K, V> {
        private final K key;
        private V value;

        public MyEntry(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }

        public void setValue(V value) {
            this.value = value;
        }

        @Override
        public String toString() {
            return "MyEntry{" +
                "key=" + key +
                ", value=" + value +
                '}';
        }
    }
}
