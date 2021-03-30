#include <iostream>
using namespace std;

void genNumbers(int array[], int size){
	for (int i=0; i<size; i++){
		array[i] = rand() % size;
	}
}

void bubbleSort(int numbers[], int size) {
	for (int i=0; i < size; i++){
		for(int j=0; j < size; j++){
			if (numbers[i] > numbers[j]){
				int tmp = numbers[i];
				numbers[i] = numbers[j];
				numbers[j] = tmp;
			}
		}
	}
}

void printNumbers(int numbers[], int size){
	for(int i=0; i < size; i++){
		cout << numbers[i] << " ";
	}
	cout << endl;
}

int main(){
	srand((int)time(0));

	int size = 10;
	int numbers[size];		
	genNumbers(numbers, size);
	
	cout << "unsorted: ";	
  printNumbers(numbers, size);

	bubbleSort(numbers, size);
	
	cout << "sorted: ";
	printNumbers(numbers, size);
}
