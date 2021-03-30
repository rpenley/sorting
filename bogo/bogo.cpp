#include <algorithm>
#include <iostream>
#include <iterator>
#include <random>
#include <vector>

// BOGOPLATE HERE
template <typename RandomAccessIterator, typename Predicate>
void bogo_sort(RandomAccessIterator begin, RandomAccessIterator end,
               Predicate p) {
  std::random_device rd;
  std::mt19937 generator(rd());
  while (!std::is_sorted(begin, end, p)) {
    std::shuffle(begin, end, generator);
  }
}

// RANDOM NUMBER LIST GENERATORPLATE (req C++14)
auto randomNumberBetween = [](int low, int high)
{
    auto randomFunc = [distribution_ = std::uniform_int_distribution<int>(low, high),
                       random_engine_ = std::mt19937{ std::random_device{}() }]() mutable
    {
        return distribution_(random_engine_);
    };
    return randomFunc;
};


template <typename RandomAccessIterator>
void bogo_sort(RandomAccessIterator begin, RandomAccessIterator end) {
  bogo_sort(
      begin, end,
      std::less<
          typename std::iterator_traits<RandomAccessIterator>::value_type>());
}

int main() {
  std::vector<int> a;
  int size;

  std::cout << "Welcome to BOGOSORT in C++! :) \n";
  std::cout << "HOW MANY ITEMS DO YOU WANT TO SORT?\n";
  std::cout << "ITEMS: ";
  std::cin >> size;
  std::generate_n(std::back_inserter(a), 10, randomNumberBetween(0, size));
  bogo_sort(std::begin(a), std::end(a));
  copy(std::begin(a), std::end(a), std::ostream_iterator<int>(std::cout, " "));

  std::cout << "\nCONGRATULATIONS YOU HAVE BOGO SORTED!!!\n";
  std::cout << "FINAL VALUES ARE...\n";
}
