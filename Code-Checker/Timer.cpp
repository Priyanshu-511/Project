#include "Timer.h"

Timer::Timer() : start_time(), end_time() {}

void Timer::start() {
    start_time = std::chrono::high_resolution_clock::now();
}

void Timer::stop() {
    end_time = std::chrono::high_resolution_clock::now();
}

long long Timer::duration() const {
    return std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time).count();
}
