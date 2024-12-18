

- optimal_training_data_size

```bash
Results for dataset maze2d-large-v1 with horizon 384, over 100 evaluation episodes:
+-------------------+-----------+-----------------+-----+----------------+--------+
|       Model       |   Prior   | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-----------+-----------------+-----+----------------+--------+
|    SBDiffusion    | BasePrior |        16       |  15 |     490000     | 104.83 |
|    SBDiffusion    | BasePrior |        16       |  15 |     400000     |  99.09 |
|    SBDiffusion    | BasePrior |        16       |  15 |     350000     | 105.91 |
|    SBDiffusion    | BasePrior |        16       |  15 |     300000     |  99.58 |
|    SBDiffusion    | BasePrior |        16       |  15 |     250000     | 104.95 |
|    SBDiffusion    | BasePrior |        16       |  15 |     200000     |  93.60 |
|    SBDiffusion    | BasePrior |        16       |  15 |     150000     | 100.50 |
|    SBDiffusion    | BasePrior |        16       |  15 |     100000     |  83.91 |
| GaussianDiffusion |     -     |        16       |  -  |     490000     | 133.53 |
| GaussianDiffusion |     -     |        16       |  -  |     400000     | 129.93 |
| GaussianDiffusion |     -     |        16       |  -  |     350000     | 131.42 |
| GaussianDiffusion |     -     |        16       |  -  |     300000     | 128.66 |
| GaussianDiffusion |     -     |        16       |  -  |     250000     | 118.37 |
| GaussianDiffusion |     -     |        16       |  -  |     200000     | 120.61 |
| GaussianDiffusion |     -     |        16       |  -  |     150000     | 124.10 |
| GaussianDiffusion |     -     |        16       |  -  |     100000     | 111.37 |
+-------------------+-----------+-----------------+-----+----------------+--------+
```




- score_vs_training_steps_for_sb_with_straight_line_prior

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------+-------------------+-----------------+-----+----------------+--------+
|    Model    |       Prior       | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+-------------------+-----------------+-----+----------------+--------+
| SBDiffusion | StraightLinePrior |        16       |  4  |     245000     | 119.02 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     200000     | 116.14 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     150000     | 113.71 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     100000     | 110.86 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     50000      | 107.90 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     25000      |  93.94 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     10000      |  83.54 |
+-------------+-------------------+-----------------+-----+----------------+--------+
```


- nfe_and_training_steps_score_sb_base_prior_maze2d_large


```bash
Results for dataset maze2d-large-v1 with horizon 384, over 200 evaluation episodes:
+-------------+-----------+-----------------+-----+----------------+--------+
|    Model    |   Prior   | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+-----------+-----------------+-----+----------------+--------+
| SBDiffusion | BasePrior |        16       |  10 |     245000     | 124.68 |
| SBDiffusion | BasePrior |        16       |  10 |     200000     | 123.38 |
| SBDiffusion | BasePrior |        16       |  10 |     150000     | 119.28 |
| SBDiffusion | BasePrior |        16       |  10 |     100000     | 108.30 |
| SBDiffusion | BasePrior |        16       |  7  |     245000     | 129.12 |
| SBDiffusion | BasePrior |        16       |  7  |     200000     | 125.16 |
| SBDiffusion | BasePrior |        16       |  7  |     150000     | 125.16 |
| SBDiffusion | BasePrior |        16       |  7  |     100000     | 120.63 |
| SBDiffusion | BasePrior |        16       |  4  |     245000     | 122.89 |
| SBDiffusion | BasePrior |        16       |  4  |     200000     | 123.47 |
| SBDiffusion | BasePrior |        16       |  4  |     150000     | 123.61 |
| SBDiffusion | BasePrior |        16       |  4  |     100000     | 114.63 |
| SBDiffusion | BasePrior |        16       |  1  |     245000     | 128.30 |
| SBDiffusion | BasePrior |        16       |  1  |     200000     | 127.11 |
| SBDiffusion | BasePrior |        16       |  1  |     150000     | 124.81 |
| SBDiffusion | BasePrior |        16       |  1  |     100000     | 127.95 |
+-------------+-----------+-----------------+-----+----------------+--------+
```

- nfe_and_training_steps_score_ddpm_maze2d_large

```bash
Results for dataset maze2d-large-v1 with horizon 384, over 200 evaluation episodes:
+-------------------+-------+-----------------+-----+----------------+--------+
|       Model       | Prior | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-------+-----------------+-----+----------------+--------+
| GaussianDiffusion |   -   |        11       |  10 |     245000     | 133.61 |
| GaussianDiffusion |   -   |        11       |  10 |     200000     | 130.17 |
| GaussianDiffusion |   -   |        11       |  10 |     150000     | 132.42 |
| GaussianDiffusion |   -   |        11       |  10 |     100000     | 115.94 |
| GaussianDiffusion |   -   |        8        |  7  |     245000     | 127.02 |
| GaussianDiffusion |   -   |        8        |  7  |     200000     | 132.92 |
| GaussianDiffusion |   -   |        8        |  7  |     150000     | 129.90 |
| GaussianDiffusion |   -   |        8        |  7  |     100000     | 122.63 |
| GaussianDiffusion |   -   |        5        |  4  |     245000     | 125.17 |
| GaussianDiffusion |   -   |        5        |  4  |     200000     | 129.52 |
| GaussianDiffusion |   -   |        5        |  4  |     150000     | 130.62 |
| GaussianDiffusion |   -   |        5        |  4  |     100000     | 125.31 |
| GaussianDiffusion |   -   |        2        |  1  |     245000     | 114.23 |
| GaussianDiffusion |   -   |        2        |  1  |     200000     | 119.71 |
| GaussianDiffusion |   -   |        2        |  1  |     150000     | 118.08 |
| GaussianDiffusion |   -   |        2        |  1  |     100000     | 114.13 |
+-------------------+-------+-----------------+-----+----------------+--------+
```




---



- nfe_and_training_steps_score_sb_base_prior_maze2d_medium

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------+-----------+-----------------+-----+----------------+--------+
|    Model    |   Prior   | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+-----------+-----------------+-----+----------------+--------+
| SBDiffusion | BasePrior |        16       |  10 |     245000     | 122.37 |
| SBDiffusion | BasePrior |        16       |  10 |     200000     | 122.38 |
| SBDiffusion | BasePrior |        16       |  10 |     150000     | 125.40 |
| SBDiffusion | BasePrior |        16       |  10 |     100000     | 122.31 |
| SBDiffusion | BasePrior |        16       |  7  |     245000     | 123.48 |
| SBDiffusion | BasePrior |        16       |  7  |     200000     | 124.60 |
| SBDiffusion | BasePrior |        16       |  7  |     150000     | 124.96 |
| SBDiffusion | BasePrior |        16       |  7  |     100000     | 122.61 |
| SBDiffusion | BasePrior |        16       |  4  |     245000     | 124.11 |
| SBDiffusion | BasePrior |        16       |  4  |     200000     | 123.87 |
| SBDiffusion | BasePrior |        16       |  4  |     150000     | 123.80 |
| SBDiffusion | BasePrior |        16       |  4  |     100000     | 123.47 |
| SBDiffusion | BasePrior |        16       |  1  |     245000     | 123.03 |
| SBDiffusion | BasePrior |        16       |  1  |     200000     | 122.27 |
| SBDiffusion | BasePrior |        16       |  1  |     150000     | 123.83 |
| SBDiffusion | BasePrior |        16       |  1  |     100000     | 123.22 |
+-------------+-----------+-----------------+-----+----------------+--------+
```

- nfe_and_training_steps_score_ddpm_maze2d_large

```bash

Results for dataset maze2d-large-v1 with horizon 384, over 200 evaluation episodes:
+-------------------+-------+-----------------+-----+----------------+--------+
|       Model       | Prior | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-------+-----------------+-----+----------------+--------+
| GaussianDiffusion |   -   |        11       |  10 |     245000     | 130.96 |
| GaussianDiffusion |   -   |        11       |  10 |     200000     | 135.61 |
| GaussianDiffusion |   -   |        11       |  10 |     150000     | 132.75 |
| GaussianDiffusion |   -   |        11       |  10 |     100000     | 134.37 |
| GaussianDiffusion |   -   |        8        |  7  |     245000     | 134.61 |
| GaussianDiffusion |   -   |        8        |  7  |     200000     | 132.84 |
| GaussianDiffusion |   -   |        8        |  7  |     150000     | 131.53 |
| GaussianDiffusion |   -   |        8        |  7  |     100000     | 128.54 |
| GaussianDiffusion |   -   |        5        |  4  |     245000     | 130.92 |
| GaussianDiffusion |   -   |        5        |  4  |     200000     | 140.61 |
| GaussianDiffusion |   -   |        5        |  4  |     150000     | 135.36 |
| GaussianDiffusion |   -   |        5        |  4  |     100000     | 133.37 |
| GaussianDiffusion |   -   |        2        |  1  |     245000     | 117.55 |
| GaussianDiffusion |   -   |        2        |  1  |     200000     | 122.73 |
| GaussianDiffusion |   -   |        2        |  1  |     150000     | 114.03 |
| GaussianDiffusion |   -   |        2        |  1  |     100000     | 113.62 |
+-------------------+-------+-----------------+-----+----------------+--------+
```


- score_vs_training_steps_for_sb_with_straight_line_prior
- 
```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------+-------------------+-----------------+-----+----------------+--------+
|    Model    |       Prior       | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+-------------------+-----------------+-----+----------------+--------+
| SBDiffusion | StraightLinePrior |        16       |  4  |     245000     | 119.28 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     200000     | 114.52 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     150000     | 113.89 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     100000     | 112.98 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     50000      | 103.09 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     25000      |  96.24 |
| SBDiffusion | StraightLinePrior |        16       |  4  |     10000      |  82.90 |
+-------------+-------------------+-----------------+-----+----------------+--------+
```


- score_vs_training_steps_for_sb_with_base_prior

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------+-----------+-----------------+-----+----------------+--------+
|    Model    |   Prior   | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+-----------+-----------------+-----+----------------+--------+
| SBDiffusion | BasePrior |        16       |  4  |     245000     | 122.79 |
| SBDiffusion | BasePrior |        16       |  4  |     200000     | 126.34 |
| SBDiffusion | BasePrior |        16       |  4  |     150000     | 123.00 |
| SBDiffusion | BasePrior |        16       |  4  |     100000     | 126.22 |
| SBDiffusion | BasePrior |        16       |  4  |     50000      | 121.11 |
| SBDiffusion | BasePrior |        16       |  4  |     25000      | 121.27 |
| SBDiffusion | BasePrior |        16       |  4  |     10000      | 111.73 |
+-------------+-----------+-----------------+-----+----------------+--------+
```


- score_vs_training_steps_for_ddpm_maze2d_medium

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------------+-------+-----------------+-----+----------------+--------+
|       Model       | Prior | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-------+-----------------+-----+----------------+--------+
| GaussianDiffusion |   -   |        5        |  -  |     150000     | 126.46 |
| GaussianDiffusion |   -   |        5        |  -  |     100000     | 127.13 |
| GaussianDiffusion |   -   |        5        |  -  |     50000      | 128.98 |
| GaussianDiffusion |   -   |        5        |  -  |     25000      | 128.04 |
| GaussianDiffusion |   -   |        5        |  -  |     10000      | 118.98 |
+-------------------+-------+-----------------+-----+----------------+--------+
```

- score_vs_training_steps_for_sb_with_MLP_prior

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------+--------------------+-----------------+-----+----------------+--------+
|    Model    |       Prior        | Diffusion Steps | NFE | Training Steps | Score  |
+-------------+--------------------+-----------------+-----+----------------+--------+
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     245000     | 124.80 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     200000     | 122.98 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     150000     | 123.71 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     100000     | 122.04 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     50000      | 121.35 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     25000      | 120.56 |
| SBDiffusion | MLPTrajectoryPrior |        16       |  4  |     10000      | 117.61 |
+-------------+--------------------+-----------------+-----+----------------+--------+

```



- score_vs_training_steps_for_ddpm_maze2d_medium


```bash

Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------------+-------+-----------------+-----+----------------+--------+
|       Model       | Prior | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-------+-----------------+-----+----------------+--------+
| GaussianDiffusion |   -   |        5        |  -  |     150000     | 123.70 |
| GaussianDiffusion |   -   |        5        |  -  |     100000     | 126.72 |
| GaussianDiffusion |   -   |        5        |  -  |     50000      | 124.24 |
| GaussianDiffusion |   -   |        5        |  -  |     25000      | 123.00 |
| GaussianDiffusion |   -   |        5        |  -  |     10000      | 117.38 |
+-------------------+-------+-----------------+-----+----------------+--------+
```

- score_vs_training_steps_for_ddpm_maze2d_medium_NFE_1
```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------------+-------+-----------------+-----+----------------+--------+
|       Model       | Prior | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+-------+-----------------+-----+----------------+--------+
| GaussianDiffusion |   -   |        2        |  -  |     245000     | 118.16 |
| GaussianDiffusion |   -   |        2        |  -  |     200000     | 116.90 |
| GaussianDiffusion |   -   |        2        |  -  |     150000     | 118.36 |
| GaussianDiffusion |   -   |        2        |  -  |     100000     | 114.37 |
+-------------------+-------+-----------------+-----+----------------+--------+
```


- score_vs_training_steps_for_ddpm_vs_sb_on_different_priors_maze2d_medium_NFE_1

```bash

Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------------+--------------------+-----------------+-----+----------------+--------+
|       Model       |       Prior        | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+--------------------+-----------------+-----+----------------+--------+
| GaussianDiffusion |         -          |        2        |  -  |     245000     | 123.33 |
| GaussianDiffusion |         -          |        2        |  -  |     200000     | 126.13 |
| GaussianDiffusion |         -          |        2        |  -  |     150000     | 122.23 |
| GaussianDiffusion |         -          |        2        |  -  |     100000     | 126.19 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     245000     | 127.29 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     200000     | 129.16 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     150000     | 128.95 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     100000     | 127.38 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     50000      | 127.62 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     25000      | 128.74 |
|    SBDiffusion    |     BasePrior      |        16       |  1  |     10000      | 129.01 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     245000     | 122.52 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     200000     | 122.20 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     150000     | 119.78 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     100000     | 116.35 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     50000      | 109.27 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     25000      |  97.74 |
|    SBDiffusion    | StraightLinePrior  |        16       |  1  |     10000      | 100.74 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     245000     | 125.60 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     200000     | 125.93 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     150000     | 124.64 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     100000     | 123.55 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     50000      | 124.57 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     25000      | 122.96 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  1  |     10000      | 120.65 |
+-------------------+--------------------+-----------------+-----+----------------+--------+

Process finished with exit code 0

```

- score_vs_training_steps_for_ddpm_vs_sb_on_different_priors_maze2d_medium_NFE_1_same_complexity

```bash
Results for dataset maze2d-medium-v1 with horizon 256, over 200 evaluation episodes:
+-------------------+--------------------+-----------------+-----+----------------+--------+
|       Model       |       Prior        | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+--------------------+-----------------+-----+----------------+--------+
| GaussianDiffusion |         -          |        2        |  -  |     245000     | 117.35 |
| GaussianDiffusion |         -          |        2        |  -  |     200000     | 117.94 |
| GaussianDiffusion |         -          |        2        |  -  |     150000     | 120.82 |
| GaussianDiffusion |         -          |        2        |  -  |     100000     | 118.98 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     245000     |  64.17 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     200000     |  63.07 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     150000     |  64.54 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     100000     |  64.60 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     50000      |  57.49 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     25000      |  59.65 |
|    SBDiffusion    |     BasePrior      |        2        |  1  |     10000      |  56.70 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     245000     |  62.77 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     200000     |  62.98 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     150000     |  63.06 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     100000     |  63.66 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     50000      |  64.03 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     25000      |  64.54 |
|    SBDiffusion    | StraightLinePrior  |        2        |  1  |     10000      |  65.41 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     245000     |  47.76 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     200000     |  47.69 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     150000     |  47.39 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     100000     |  47.04 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     50000      |  46.72 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     25000      |  46.85 |
|    SBDiffusion    | MLPTrajectoryPrior |        2        |  1  |     10000      |  46.72 |
+-------------------+--------------------+-----------------+-----+----------------+--------+
```

- score_vs_training_steps_for_ddpm_vs_sb_on_different_priors_maze2d_medium_T_64_NFE_1

```bash
+-------------------+--------------------+-----------------+-----+----------------+--------+
|       Model       |       Prior        | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+--------------------+-----------------+-----+----------------+--------+
| GaussianDiffusion |         -          |        2        |  -  |     245000     | 119.35 |
| GaussianDiffusion |         -          |        2        |  -  |     200000     | 121.32 |
| GaussianDiffusion |         -          |        2        |  -  |     150000     | 119.98 |
| GaussianDiffusion |         -          |        2        |  -  |     100000     | 120.74 |
| GaussianDiffusion |         -          |        2        |  -  |     50000      | 122.09 |
| GaussianDiffusion |         -          |        2        |  -  |     25000      | 121.68 |
| GaussianDiffusion |         -          |        2        |  -  |     10000      | 119.88 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     245000     | 122.04 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     200000     | 123.59 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     150000     | 121.31 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     100000     | 124.16 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     50000      | 121.60 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     25000      | 124.47 |
|    SBDiffusion    |     BasePrior      |        64       |  1  |     10000      | 121.37 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     245000     | 120.10 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     200000     | 122.62 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     150000     | 123.14 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     100000     | 124.05 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     50000      | 120.84 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     25000      | 116.11 |
|    SBDiffusion    | StraightLinePrior  |        64       |  1  |     10000      | 115.04 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     245000     | 123.06 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     200000     | 122.93 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     150000     | 121.83 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     100000     | 124.18 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     50000      | 120.67 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     25000      | 121.33 |
|    SBDiffusion    | MLPTrajectoryPrior |        64       |  1  |     10000      | 117.08 |
+-------------------+--------------------+-----------------+-----+----------------+--------+
```


```
+-------------------+--------------------+-----------------+-----+----------------+--------+
|       Model       |       Prior        | Diffusion Steps | NFE | Training Steps | Score  |
+-------------------+--------------------+-----------------+-----+----------------+--------+
|    SBDiffusion    |     BasePrior      |        16       |  4  |     245000     | 126.15 |
|    SBDiffusion    |     BasePrior      |        16       |  4  |     200000     | 119.24 |
|    SBDiffusion    |     BasePrior      |        16       |  4  |     150000     | 118.40 |
|    SBDiffusion    |     BasePrior      |        16       |  4  |     100000     | 111.97 |
|    SBDiffusion    | StraightLinePrior  |        16       |  4  |     245000     | 118.29 |
|    SBDiffusion    | StraightLinePrior  |        16       |  4  |     200000     | 117.13 |
|    SBDiffusion    | StraightLinePrior  |        16       |  4  |     150000     | 114.64 |
|    SBDiffusion    | StraightLinePrior  |        16       |  4  |     100000     | 112.54 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  4  |     245000     | 124.80 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  4  |     200000     | 122.98 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  4  |     150000     | 123.71 |
|    SBDiffusion    | MLPTrajectoryPrior |        16       |  4  |     100000     | 122.04 |
+-------------------+--------------------+-----------------+-----+----------------+--------+
```