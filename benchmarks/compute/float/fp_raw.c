#include <stdlib.h>
#include <time.h>
#include <stdio.h>

#define OPTIMIZE3 	__attribute__((optimize("-O3")));

#define LOOP_TIMES 1000000

#define TYPE float

#pragma GCC push_options
#pragma GCC optimize ("O0")
static int OPTIMIZE3 add_u32() {
    unsigned int i;
	double t;
    register TYPE r0, r1;//, r2, r3;
    register TYPE i0, i1;//, i2, i3;
	struct timespec start_time, end_time;

    // generate random ints
    r0 = rand();
    r1 = rand();
    // r2 = rand();
    // r3 = rand();

    i0 = rand();
    i1 = rand();
    // i2 = rand();
    // i3 = rand();


    clock_gettime(CLOCK_MONOTONIC, &start_time);
    for (size_t i = 0; i < LOOP_TIMES; i++)
    {
        r0 += i0;
		r1 += i1;
		// r2 += i2;
		// r3 += i3;

		i0 += r0;
		i1 += r1;
		// i2 += r2;
		// i3 += r3;
    }
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    t = (end_time.tv_sec - start_time.tv_sec) * 1e9;
    t += (end_time.tv_nsec - start_time.tv_nsec);
    t /= 1e3;

    printf("add_u32 time us: %f\n", t);
    return 1;
}

double addi_t = 0;
static int addi_u32() {
    unsigned int i;
    register TYPE r0, r1;//, r2, r3;
    register TYPE i0, i1;//, i2, i3;
    struct timespec start_time, end_time;

    // generate random ints
    r0 = rand();
    r1 = rand();
    // r2 = rand();
    // r3 = rand();

    i0 = rand();
    i1 = rand();
    // i2 = rand();
    // i3 = rand();

    clock_gettime(CLOCK_MONOTONIC, &start_time);
    for (size_t i = 0; i < LOOP_TIMES; i++)
    {
        r0 += 0xdeadbeef;
        r1 += 0xdeadbeef;
        // r2 += 0xdeadbeef;
        // r3 += 0xdeadbeef;

        i0 += 0xdeadbeef;
        i1 += 0xdeadbeef;
        // i2 += 0xdeadbeef;
        // i3 += 0xdeadbeef;
    }
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    addi_t = (end_time.tv_sec - start_time.tv_sec) * 1e9;
    addi_t += (end_time.tv_nsec - start_time.tv_nsec);
    addi_t /= 1e3;

    printf("addi_u32 time us: %f\n", addi_t);
    return 1;

}

static int sub_u32() {
    unsigned int i;
    double t;
    register TYPE r0, r1;//, r2, r3;
    register TYPE i0, i1;//, i2, i3;
    struct timespec start_time, end_time;

    // generate random ints
    r0 = rand();
    r1 = rand();
    // r2 = rand();
    // r3 = rand();

    i0 = rand();
    i1 = rand();
    // i2 = rand();
    // i3 = rand();

    clock_gettime(CLOCK_MONOTONIC, &start_time);
    for (size_t i = 0; i < LOOP_TIMES; i++)
    {
        r0 -= i0;
		r1 -= i1;

		i0 -= r0;
		i1 -= r1;
    }
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    t = (end_time.tv_sec - start_time.tv_sec) * 1e9;
    t += (end_time.tv_nsec - start_time.tv_nsec);
    t /= 1e3;

    printf("sub_u32 time us: %f\n", t);
    return 1;
}

static int mul_u32() {
    unsigned int i;
    double t;
    register TYPE r0, r1;//, r2, r3;
    register TYPE i0, i1;//, i2, i3;
    struct timespec start_time, end_time;

    // generate random ints
    r0 = rand();
    r1 = rand();
    // r2 = rand();
    // r3 = rand();

    i0 = rand();
    i1 = rand();
    // i2 = rand();
    // i3 = rand();

    clock_gettime(CLOCK_MONOTONIC, &start_time);
    for (size_t i = 0; i < LOOP_TIMES; i++)
    {
        r0 *= i0;
        r1 *= i1;

        i0 *= r0;
        i1 *= r1;
    }
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    t = (end_time.tv_sec - start_time.tv_sec) * 1e9;
    t += (end_time.tv_nsec - start_time.tv_nsec);
    t /= 1e3;

    printf("mul_u32 time us: %f\n", t);
    return 1;
}

static int div_u32() {
    unsigned int i;
    double t = 0;
    register TYPE r0, r1;//, r2, r3;
    register TYPE i0, i1;//, i2, i3;
    struct timespec start_time, end_time;

    // generate random ints
    r0 = rand();
    r1 = rand();
    // r2 = rand();
    // r3 = rand();

    i0 = rand();
    i1 = rand();
    // i2 = rand();
    // i3 = rand();

    clock_gettime(CLOCK_MONOTONIC, &start_time);
    for (size_t i = 0; i < LOOP_TIMES; i++)
    {
        // r0 *= i0;
        // r1 *= i1;

        // i0 *= r0;
        // i1 *= r1;
        
        i0 += 0xdeadbeef;
        i1 += 0xdeadbeef;
        r0 /= i0;
        r1 /= i1;

        r0 += 0xdeadbeef;
        r1 += 0xdeadbeef;
        i0 /= r0;
        i1 /= r1;
    }
    clock_gettime(CLOCK_MONOTONIC, &end_time);

    t += (end_time.tv_sec - start_time.tv_sec) * 1e9;
    t += (end_time.tv_nsec - start_time.tv_nsec);
    t /= 1e3;

    printf("div_u32 time us: %f\n", t - addi_t);
    return 1;
}

int main() {
    add_u32();
    addi_u32();
    sub_u32();
    mul_u32();
    div_u32();
    return 0;
}