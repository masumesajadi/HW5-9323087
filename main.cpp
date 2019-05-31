#include <iostream>
#include <random>
#include <algorithm>
#include <vector>
#include <chrono>
#include <numeric>
#include <execution>


void print_Vector(std::vector<int>& vec);
int  fill(int a, int b, std::vector<int>& v);



int main()
{
	std::vector<int> vec1;
	std::vector<int> vec2;
	std::vector<int> revers_vec;

	fill(1, 101, vec1);
	std::cout << "vec1  ";
	print_Vector(vec1);

	fill(1, 11, vec2);
	std::cout << "vec2  ";
	print_Vector(vec2);

	// vector + vector
	vec2.insert(vec2.end(), vec1.begin(), vec1.end());
	std::cout << "vec2 = vec1 + vec2  ";
	print_Vector(vec2);

	// odd numbers
	std::vector<int> odd_vec(vec1.size());
	auto end_odd_vec = std::copy_if(begin(vec1), end(vec1), begin(odd_vec),
		[](int n) { return n % 2 == 1; });
	odd_vec.erase(end_odd_vec, end(odd_vec));
	std::cout << "odd_vec  ";
	print_Vector(odd_vec);

	// reverse
	revers_vec = vec1;
	std::reverse(revers_vec.begin(), revers_vec.end());
	std::cout << "reverse_vec‬‬ ";
	print_Vector(revers_vec);

	//standard sequential sort
	sort(vec2.begin(), vec2.end());
	std::cout<< "standard sequential sort of vec2 ";
	print_Vector(vec2);

	// sequential execution
	std::sort(std::execution::seq, vec2.begin(), vec2.end());
	std::cout << "sequential execution vec2 ";
	print_Vector(vec2);
	
	//sortet Parallel vec2
	std::sort (std::execution::par, vec2.begin(), vec2.end());
	std::cout<< "sortet Parallel vec2 ";
	print_Vector(vec2);

	return 0;
}



// How to fill the Container without loop :
int fill(int a, int b, std::vector<int>& v) {
	int cnt{};
	if (a >= b)
		cnt = 100;
	else {
		v.push_back(a);
		return fill(a + 1, b, v);
	}

}


// Print Elements of Container
void print_Vector(std::vector<int>& vec) {
	std::cout << "by " << vec.size() << " elements : " << std::endl;
	auto print = [](const int& n) { std::cout << " " << n; };
	std::for_each(vec.begin(), vec.end(), print);
	std::cout << std::endl << std::endl;
}

// END OF PROGRAM
