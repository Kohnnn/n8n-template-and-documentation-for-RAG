---
url: "https://qdrant.tech/benchmarks/filter-result-2023-02-03.json"
title: undefined
---

```json
[
  {
    "engine_name": "milvus",
    "p95_time": 0.12982259434756996,
    "rps": 120.77926866562062,
    "p99_time": 0.33030459305686277,
    "mean_time": 0.06471361731390061,
    "mean_precisions": 0.604392,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "range-100-filters",
    "parallel": 8,
    "upload_time": 59.75058772099874,
    "total_upload_time": 265.2509193040023
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.005608127002778929,
    "rps": 795.0263486175817,
    "p99_time": 0.006103408988128651,
    "mean_time": 0.004048252291577228,
    "mean_precisions": 0.9704,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "int-2048-filters",
    "parallel": 8,
    "upload_time": 22.219641577001312,
    "total_upload_time": 277.6293579379999
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.060869867632573,
    "rps": 282.92141504260036,
    "p99_time": 0.14476332241698436,
    "mean_time": 0.028075038691749796,
    "mean_precisions": 0.5733560000000001,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-filters",
    "parallel": 8,
    "upload_time": 554.1917532700172,
    "total_upload_time": 554.191795871011
  },
  {
    "engine_name": "qdrant",
    "upload_time": 28.97847600300156,
    "total_upload_time": 249.3211906889992,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "keyword-100-no-filters",
    "parallel": 8,
    "p95_time": 0.0031238170491633354,
    "rps": 2836.5722185742325,
    "p99_time": 0.0035361650094273512,
    "mean_time": 0.002697261688618528,
    "mean_precisions": 0.40851000000000004,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "p95_time": 0.022843891149932457,
    "rps": 448.9892266818918,
    "p99_time": 0.02490340400010382,
    "mean_time": 0.017448292600000106,
    "mean_precisions": 0.99998,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "int-2048-filters",
    "parallel": 8,
    "upload_time": 495.76699126700987,
    "total_upload_time": 495.7670325680083
  },
  {
    "engine_name": "weaviate",
    "upload_time": 143.62152541299292,
    "total_upload_time": 143.62156651400437,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "keyword-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.050718566452997035,
    "rps": 221.70151365075372,
    "p99_time": 0.060055405105522375,
    "mean_time": 0.035850639687350486,
    "mean_precisions": 0.3832,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "upload_time": 54.541048525003134,
    "total_upload_time": 261.07416708700475,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "keyword-100-no-filters",
    "parallel": 8,
    "p95_time": 0.012880113955179694,
    "rps": 774.6808321866039,
    "p99_time": 0.015853171006310736,
    "mean_time": 0.008910100677330047,
    "mean_precisions": 0.43728999999999996,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.157336204846797,
    "rps": 140.35900315185233,
    "p99_time": 0.2360867739326205,
    "mean_time": 0.0555332157576835,
    "mean_precisions": 1.0,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "geo-radius-100-filters",
    "parallel": 8,
    "upload_time": 475.7346445269941,
    "total_upload_time": 477.12151631200686
  },
  {
    "engine_name": "redis",
    "p95_time": 0.005800681004620855,
    "rps": 1510.4876239399598,
    "p99_time": 0.0064380440185777855,
    "mean_time": 0.005160128694916785,
    "mean_precisions": 0.35083000000000003,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "keyword-100-no-filters",
    "parallel": 8,
    "upload_time": 966.5737362880027,
    "total_upload_time": 966.5737733889982
  },
  {
    "engine_name": "redis",
    "p95_time": 1.5075310595915652,
    "rps": 10.113829593370602,
    "p99_time": 1.518353780086909,
    "mean_time": 0.7906458924697246,
    "mean_precisions": 0.8291,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "keyword-100-filters",
    "parallel": 8,
    "upload_time": 838.4703913549893,
    "total_upload_time": 838.4704293549876
  },
  {
    "engine_name": "weaviate",
    "upload_time": 122.63801413701731,
    "total_upload_time": 122.63805843700538,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "int-2048-filters",
    "parallel": 8,
    "p95_time": 0.047128153949984146,
    "rps": 251.1394573007941,
    "p99_time": 0.056348523010124156,
    "mean_time": 0.0315921690511997,
    "mean_precisions": 0.999944,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.8063753138980245,
    "rps": 20.109630573645852,
    "p99_time": 1.0353704040343301,
    "mean_time": 0.3962033908148063,
    "mean_precisions": 0.9971646666666667,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "keyword-100-filters",
    "parallel": 8,
    "upload_time": 57.57094088598387,
    "total_upload_time": 160.5499015499954
  },
  {
    "engine_name": "weaviate",
    "upload_time": 109.12138237699992,
    "total_upload_time": 109.12142707700013,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "int-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.04763528000003134,
    "rps": 242.01048594374012,
    "p99_time": 0.05722024617983607,
    "mean_time": 0.03280385269010212,
    "mean_precisions": 0.38561,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "upload_time": 82.25150109099923,
    "total_upload_time": 336.9116750150024,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-no-filters",
    "parallel": 8,
    "p95_time": 0.029642398052965282,
    "rps": 406.3864266601771,
    "p99_time": 0.041818209090561165,
    "mean_time": 0.01826728132031967,
    "mean_precisions": 0.37186,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "p95_time": 0.006258136701580952,
    "rps": 1386.2124272850974,
    "p99_time": 0.006548661968990928,
    "mean_time": 0.005615831368296495,
    "mean_precisions": 0.34798,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "range-100-no-filters",
    "parallel": 8,
    "upload_time": 1061.5719955159984,
    "total_upload_time": 1061.572033217999
  },
  {
    "engine_name": "elastic",
    "upload_time": 1115.3281315459972,
    "total_upload_time": 1119.7822107840002,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-no-filters",
    "parallel": 8,
    "p95_time": 0.5611648967978908,
    "rps": 18.175468376723188,
    "p99_time": 0.6163803898898187,
    "mean_time": 0.4386204439509835,
    "mean_precisions": 0.9102000000000002,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "weaviate",
    "upload_time": 1481.3664408480108,
    "total_upload_time": 1481.366480947996,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "geo-radius-100-filters",
    "parallel": 8,
    "p95_time": 0.11494665406207782,
    "rps": 172.6765259126334,
    "p99_time": 0.14929579722404018,
    "mean_time": 0.04616029768351291,
    "mean_precisions": 0.2183205576601462,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 485.82856437400187,
    "total_upload_time": 485.8286052750045,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "range-2048-filters",
    "parallel": 8,
    "p95_time": 0.6128989070057286,
    "rps": 16.118820859479097,
    "p99_time": 0.6613555148498563,
    "mean_time": 0.4947511775325373,
    "mean_precisions": 0.9999400000000002,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.005861685746276634,
    "rps": 786.0760783411241,
    "p99_time": 0.006173147998415516,
    "mean_time": 0.0047969017622002865,
    "mean_precisions": 0.4645,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "geo-radius-2048-no-filters",
    "parallel": 8,
    "upload_time": 21.70322822700109,
    "total_upload_time": 151.90829814300378
  },
  {
    "engine_name": "redis",
    "p95_time": 0.020169364349612806,
    "rps": 407.3920935567137,
    "p99_time": 0.020606488999956128,
    "mean_time": 0.019191185450904324,
    "mean_precisions": 0.3872,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "int-2048-no-filters",
    "parallel": 8,
    "upload_time": 406.9211787809995,
    "total_upload_time": 406.9212192809996
  },
  {
    "engine_name": "redis",
    "upload_time": 915.1605211479764,
    "total_upload_time": 915.1605836489762,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "geo-radius-100-filters",
    "parallel": 8,
    "p95_time": 1.791391758150712,
    "rps": 8.656094524614728,
    "p99_time": 2.2478878810125753,
    "mean_time": 0.9236492921782454,
    "mean_precisions": 0.8333458160256981,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 445.8485472709872,
    "total_upload_time": 445.8485969720059,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "geo-radius-2048-filters",
    "parallel": 8,
    "p95_time": 0.08984521183592732,
    "rps": 134.2993842755739,
    "p99_time": 0.10501881881238662,
    "mean_time": 0.05922382188074116,
    "mean_precisions": 0.9480563947397969,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.18496641659585267,
    "rps": 66.04649323896643,
    "p99_time": 0.29601926347619156,
    "mean_time": 0.11973613396540023,
    "mean_precisions": 0.323644,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "range-100-filters",
    "parallel": 8,
    "upload_time": 475.46510337200016,
    "total_upload_time": 476.54928892799944
  },
  {
    "engine_name": "weaviate",
    "upload_time": 520.9735126099986,
    "total_upload_time": 520.9735491110041,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "keyword-100-no-filters",
    "parallel": 8,
    "p95_time": 0.009588372007419818,
    "rps": 1059.7365501858592,
    "p99_time": 0.015072612006333658,
    "mean_time": 0.007428906473929237,
    "mean_precisions": 0.34578000000000003,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 21.177114682999672,
    "total_upload_time": 206.47353705800197,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "geo-radius-2048-filters",
    "parallel": 8,
    "p95_time": 0.017590238004049748,
    "rps": 732.1556444569409,
    "p99_time": 0.02283004900047672,
    "mean_time": 0.008105848879181575,
    "mean_precisions": 0.999944,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.36310681910399567,
    "rps": 46.71067856047857,
    "p99_time": 0.41489248535042866,
    "mean_time": 0.1696174883954547,
    "mean_precisions": 0.99898,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "keyword-2048-filters",
    "parallel": 8,
    "upload_time": 32.16871961101424,
    "total_upload_time": 152.43981072001043
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.07729883655847511,
    "rps": 222.5373744842224,
    "p99_time": 0.11192101585649655,
    "mean_time": 0.034516317807961605,
    "mean_precisions": 0.999992,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "int-100-filters",
    "parallel": 8,
    "upload_time": 459.4876422609959,
    "total_upload_time": 462.42494055099087
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.14734690299956127,
    "rps": 71.34278311847541,
    "p99_time": 0.15623546197166432,
    "mean_time": 0.11056773011035985,
    "mean_precisions": 0.7593840000000001,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-filters",
    "parallel": 8,
    "upload_time": 81.69273303600494,
    "total_upload_time": 377.06389994500205
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.009620531499240312,
    "rps": 1062.2042728705608,
    "p99_time": 0.013875493130908585,
    "mean_time": 0.007407869619761914,
    "mean_precisions": 0.34663,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "geo-radius-100-no-filters",
    "parallel": 8,
    "upload_time": 519.872436575999,
    "total_upload_time": 519.8724719769998
  },
  {
    "engine_name": "qdrant",
    "upload_time": 29.99985824000032,
    "total_upload_time": 245.31883438799923,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "int-100-no-filters",
    "parallel": 8,
    "p95_time": 0.0031639470023947062,
    "rps": 2858.269445677179,
    "p99_time": 0.0036200649984311907,
    "mean_time": 0.0026772695214829583,
    "mean_precisions": 0.41426999999999997,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.046353282072232084,
    "rps": 253.69823600613068,
    "p99_time": 0.053960035070485905,
    "mean_time": 0.03127259453528386,
    "mean_precisions": 0.9999720000000001,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "keyword-2048-filters",
    "parallel": 8,
    "upload_time": 122.54789987299591,
    "total_upload_time": 122.54794927401235
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.1421076064452791,
    "rps": 88.12338820766736,
    "p99_time": 0.165830006032993,
    "mean_time": 0.08906599569499303,
    "mean_precisions": 0.7929414035087718,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "range-2048-filters",
    "parallel": 8,
    "upload_time": 30.720292894999147,
    "total_upload_time": 194.89683629100182
  },
  {
    "engine_name": "redis",
    "upload_time": 443.29204641900003,
    "total_upload_time": 443.29208861899997,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "keyword-2048-filters",
    "parallel": 8,
    "p95_time": 0.0026592479844111945,
    "rps": 829.8828332820522,
    "p99_time": 0.002880225987173617,
    "mean_time": 0.002121267299880856,
    "mean_precisions": 0.999984,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 1412.8715842890088,
    "total_upload_time": 1412.8716218899935,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-filters",
    "parallel": 8,
    "p95_time": 0.297094133750943,
    "rps": 45.88637886156335,
    "p99_time": 0.35322255592676827,
    "mean_time": 0.1740547881387989,
    "mean_precisions": 0.648188,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "upload_time": 536.4639212910006,
    "total_upload_time": 536.4639586920002,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "int-100-no-filters",
    "parallel": 8,
    "p95_time": 0.009744642949135594,
    "rps": 1014.3358031658341,
    "p99_time": 0.013857250001638025,
    "mean_time": 0.0077658940107003215,
    "mean_precisions": 0.34757000000000005,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.024528585844382174,
    "rps": 559.7157977967821,
    "p99_time": 0.04912558073236155,
    "mean_time": 0.012910699559454224,
    "mean_precisions": 0.999992,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "keyword-100-filters",
    "parallel": 8,
    "upload_time": 487.35247248600353,
    "total_upload_time": 488.02600539900595
  },
  {
    "engine_name": "weaviate",
    "upload_time": 143.9998227670003,
    "total_upload_time": 143.99986326800718,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "geo-radius-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.05146398955839686,
    "rps": 219.20944365209706,
    "p99_time": 0.06115044676029358,
    "mean_time": 0.03626423271731328,
    "mean_precisions": 0.39608000000000004,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.0037486149962205674,
    "rps": 790.3197043584108,
    "p99_time": 0.0039076181428390555,
    "mean_time": 0.002878892406875093,
    "mean_precisions": 0.999992,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "keyword-2048-filters",
    "parallel": 8,
    "upload_time": 20.6067078499982,
    "total_upload_time": 160.83375699700264
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.6134412180981599,
    "rps": 25.186735037014266,
    "p99_time": 0.6538540944538546,
    "mean_time": 0.31596671214540545,
    "mean_precisions": 0.9492480000000001,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "int-100-filters",
    "parallel": 8,
    "upload_time": 51.12789311699453,
    "total_upload_time": 215.94835573100136
  },
  {
    "engine_name": "elastic",
    "upload_time": 515.2994288530026,
    "total_upload_time": 520.4804114120016,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "geo-radius-100-no-filters",
    "parallel": 8,
    "p95_time": 0.13859120500110292,
    "rps": 79.40998576370718,
    "p99_time": 0.17275558919009204,
    "mean_time": 0.09933309715480391,
    "mean_precisions": 0.92376,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "milvus",
    "upload_time": 52.60636030999922,
    "total_upload_time": 242.23675853200075,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "range-100-no-filters",
    "parallel": 8,
    "p95_time": 0.012965567998617188,
    "rps": 772.6885397474952,
    "p99_time": 0.016011852002993696,
    "mean_time": 0.008927152314485284,
    "mean_precisions": 0.43555,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "upload_time": 467.7271795439883,
    "total_upload_time": 467.7272294439899,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "int-100-filters",
    "parallel": 8,
    "p95_time": 0.03325140103843296,
    "rps": 403.46968528090326,
    "p99_time": 0.044790432089648724,
    "mean_time": 0.019682756938808596,
    "mean_precisions": 0.9999959999999999,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.010619221997512793,
    "rps": 1118.8951442866735,
    "p99_time": 0.024652249003083857,
    "mean_time": 0.00700474982189371,
    "mean_precisions": 0.4396960000000001,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "range-100-filters",
    "parallel": 8,
    "upload_time": 44.026487107999856,
    "total_upload_time": 680.002582219
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.01175759505276801,
    "rps": 1135.1996266598774,
    "p99_time": 0.0182420709944563,
    "mean_time": 0.006922761877891026,
    "mean_precisions": 0.9999959999999999,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "keyword-100-filters",
    "parallel": 8,
    "upload_time": 468.52291718201013,
    "total_upload_time": 468.522957683017
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.13323969915800263,
    "rps": 81.09959186171024,
    "p99_time": 0.16343618290382442,
    "mean_time": 0.09723987749682128,
    "mean_precisions": 0.9246500000000002,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "keyword-100-no-filters",
    "parallel": 8,
    "upload_time": 490.7401573880052,
    "total_upload_time": 494.65733043699584
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.01574475729985352,
    "rps": 648.6680026858247,
    "p99_time": 0.019000872839897057,
    "mean_time": 0.01091605143629513,
    "mean_precisions": 0.4975,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "int-100-no-filters",
    "parallel": 8,
    "upload_time": 78.72983046599984,
    "total_upload_time": 232.64855881899894
  },
  {
    "engine_name": "redis",
    "upload_time": 1636.0822675710006,
    "total_upload_time": 1636.0823092719984,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-no-filters",
    "parallel": 8,
    "p95_time": 0.009207419752056011,
    "rps": 922.1595619227377,
    "p99_time": 0.009952401931259375,
    "mean_time": 0.008525551204292787,
    "mean_precisions": 0.19169,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.013235293002071557,
    "rps": 787.7313576674836,
    "p99_time": 0.018220572989375797,
    "mean_time": 0.010029493666002963,
    "mean_precisions": 0.19227000000000002,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-no-filters",
    "parallel": 8,
    "upload_time": 639.563576671997,
    "total_upload_time": 639.5636130729981
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.005000024002220016,
    "rps": 786.7893069494593,
    "p99_time": 0.0054601339994405865,
    "mean_time": 0.004644836804032821,
    "mean_precisions": 0.44006000000000006,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "keyword-2048-no-filters",
    "parallel": 8,
    "upload_time": 21.16267428399442,
    "total_upload_time": 166.392119473996
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.003291835002710286,
    "rps": 2804.838598794213,
    "p99_time": 0.003676720998591918,
    "mean_time": 0.0027276493623990972,
    "mean_precisions": 0.39121999999999996,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "range-100-no-filters",
    "parallel": 8,
    "upload_time": 31.92236971999955,
    "total_upload_time": 217.20962560399857
  },
  {
    "engine_name": "qdrant",
    "upload_time": 52.32986951500061,
    "total_upload_time": 558.1255640999952,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-filters",
    "parallel": 8,
    "p95_time": 0.02944726935093058,
    "rps": 627.5556775093376,
    "p99_time": 0.031606826155111775,
    "mean_time": 0.012589726932167832,
    "mean_precisions": 0.597504,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "p95_time": 2.190688422401581,
    "rps": 5.290801100125922,
    "p99_time": 2.437438242052887,
    "mean_time": 1.5112793747136777,
    "mean_precisions": 0.318576,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "range-100-filters",
    "parallel": 8,
    "upload_time": 1054.5999018970033,
    "total_upload_time": 1054.5999398980057
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.009945446954225189,
    "rps": 769.1195207661337,
    "p99_time": 0.010730602990079207,
    "mean_time": 0.007922043598245363,
    "mean_precisions": 0.5479400000000001,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "range-2048-filters",
    "parallel": 8,
    "upload_time": 22.13764601600269,
    "total_upload_time": 262.5193815070015
  },
  {
    "engine_name": "redis",
    "p95_time": 0.005750621049628535,
    "rps": 1557.7678253131942,
    "p99_time": 0.007125831007033418,
    "mean_time": 0.00500020346040219,
    "mean_precisions": 0.34591,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "geo-radius-100-no-filters",
    "parallel": 8,
    "upload_time": 958.1770300280004,
    "total_upload_time": 958.1770738289997
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.0029541370022343467,
    "rps": 2928.093543670165,
    "p99_time": 0.0033542139967903495,
    "mean_time": 0.0026115019791730447,
    "mean_precisions": 0.40060999999999997,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "geo-radius-100-no-filters",
    "parallel": 8,
    "upload_time": 29.158808702995884,
    "total_upload_time": 249.50327014199866
  },
  {
    "engine_name": "qdrant",
    "upload_time": 22.486673500003235,
    "total_upload_time": 137.6705067340008,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "int-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.0059176620448852186,
    "rps": 797.945924918874,
    "p99_time": 0.0062274710012570735,
    "mean_time": 0.00485985884118345,
    "mean_precisions": 0.44228999999999996,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 89.46155621099751,
    "total_upload_time": 555.1911257719948,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "geo-radius-100-filters",
    "parallel": 8,
    "p95_time": 0.1321094797498517,
    "rps": 179.98675630989246,
    "p99_time": 0.17196232572721784,
    "mean_time": 0.0442063328730801,
    "mean_precisions": 0.9999236666666668,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "p95_time": 0.8161017308637383,
    "rps": 21.160287525288215,
    "p99_time": 0.9068239592094324,
    "mean_time": 0.37647403334884727,
    "mean_precisions": 0.99656,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    },
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-filters",
    "parallel": 8,
    "upload_time": 1033.7692494200019,
    "total_upload_time": 1035.096368094004
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.004165975997966597,
    "rps": 2276.172626254992,
    "p99_time": 0.005230250985259773,
    "mean_time": 0.0033863911997941616,
    "mean_precisions": 0.29512000000000005,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "100-kw-small-vocab-no-filters",
    "parallel": 8,
    "upload_time": 42.97816371600493,
    "total_upload_time": 248.2971040190023
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.09291366845573065,
    "rps": 114.3922204123433,
    "p99_time": 0.11355346848882618,
    "mean_time": 0.06784756681115105,
    "mean_precisions": 0.74428,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "range-2048-no-filters",
    "parallel": 8,
    "upload_time": 30.47325847799948,
    "total_upload_time": 120.33686070599651
  },
  {
    "engine_name": "redis",
    "upload_time": 840.132846353983,
    "total_upload_time": 840.1328861539951,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "int-100-filters",
    "parallel": 8,
    "p95_time": 0.05375603697320912,
    "rps": 171.46616001971617,
    "p99_time": 0.055994554973731285,
    "mean_time": 0.046456831378120116,
    "mean_precisions": 0.9999959999999999,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.0056671420010388825,
    "rps": 788.6556432165739,
    "p99_time": 0.006009624010839616,
    "mean_time": 0.004641086361414636,
    "mean_precisions": 0.45832,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "range-2048-no-filters",
    "parallel": 8,
    "upload_time": 21.835920031997375,
    "total_upload_time": 147.03254608400312
  },
  {
    "engine_name": "redis",
    "p95_time": 0.030877801495807943,
    "rps": 270.3147111630208,
    "p99_time": 0.031656928005832016,
    "mean_time": 0.02931836484870146,
    "mean_precisions": 0.3836,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "range-2048-no-filters",
    "parallel": 8,
    "upload_time": 506.6514792860107,
    "total_upload_time": 506.65152058700914
  },
  {
    "engine_name": "weaviate",
    "upload_time": 174.91833851399133,
    "total_upload_time": 174.9183873150032,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "geo-radius-2048-filters",
    "parallel": 8,
    "p95_time": 0.11534301460051208,
    "rps": 137.67474193859243,
    "p99_time": 0.14974161304096928,
    "mean_time": 0.05782824723286612,
    "mean_precisions": 0.6744883101102057,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.08406510010463533,
    "rps": 130.1308300203729,
    "p99_time": 0.09882820938204534,
    "mean_time": 0.05867269104287552,
    "mean_precisions": 0.74911,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "keyword-2048-no-filters",
    "parallel": 8,
    "upload_time": 47.417717465999885,
    "total_upload_time": 138.1754566890013
  },
  {
    "engine_name": "elastic",
    "upload_time": 548.7518933770007,
    "total_upload_time": 553.2957439420006,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "int-100-no-filters",
    "parallel": 8,
    "p95_time": 0.1446563163499377,
    "rps": 78.77330737337881,
    "p99_time": 0.17692758742143294,
    "mean_time": 0.10010966221569943,
    "mean_precisions": 0.9227900000000001,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "elastic",
    "upload_time": 519.3798396700004,
    "total_upload_time": 523.8665533050007,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "range-100-no-filters",
    "parallel": 8,
    "p95_time": 0.14603285754910755,
    "rps": 77.22252931266763,
    "p99_time": 0.1757026299299834,
    "mean_time": 0.10216345878650136,
    "mean_precisions": 0.9212400000000002,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "redis",
    "p95_time": 0.0060386829498384025,
    "rps": 1443.014195665719,
    "p99_time": 0.006477670540261897,
    "mean_time": 0.0053930150420992504,
    "mean_precisions": 0.34624,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "int-100-no-filters",
    "parallel": 8,
    "upload_time": 994.8033701059994,
    "total_upload_time": 994.8034092070011
  },
  {
    "engine_name": "redis",
    "upload_time": 502.58679859699623,
    "total_upload_time": 502.5868418979953,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "geo-radius-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.029857884999364613,
    "rps": 279.5674379732322,
    "p99_time": 0.03067927898999187,
    "mean_time": 0.02816103406593029,
    "mean_precisions": 0.39413000000000004,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 38.357689918997494,
    "total_upload_time": 258.7076136529977,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "keyword-100-filters",
    "parallel": 8,
    "p95_time": 0.004413552999722014,
    "rps": 2286.9565803922014,
    "p99_time": 0.004748964000100387,
    "mean_time": 0.0033577877566040113,
    "mean_precisions": 1.0,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 48.3694588210019,
    "total_upload_time": 829.5508513530003,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "int-100-filters",
    "parallel": 8,
    "p95_time": 0.00914454699941416,
    "rps": 1260.082373011253,
    "p99_time": 0.009769336033023138,
    "mean_time": 0.006203781836326016,
    "mean_precisions": 0.9999959999999999,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 515.9993545390025,
    "total_upload_time": 515.9994124410005,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "keyword-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.030991847954283003,
    "rps": 268.75913681611553,
    "p99_time": 0.031979337995580864,
    "mean_time": 0.028975626277393893,
    "mean_precisions": 0.37781,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "p95_time": 0.09209753295581319,
    "rps": 208.57316353186144,
    "p99_time": 0.12206588805944203,
    "mean_time": 0.036414387586255904,
    "mean_precisions": 0.4789638095238095,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    },
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "h-and-m-2048-filters",
    "parallel": 8,
    "upload_time": 178.78241364699988,
    "total_upload_time": 178.78244824700005
  },
  {
    "engine_name": "milvus",
    "p95_time": 0.040724509749861665,
    "rps": 270.00125654696876,
    "p99_time": 0.06324362501994076,
    "mean_time": 0.024818959924998763,
    "mean_precisions": 0.99939,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    },
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "h-and-m-2048-no-filters",
    "parallel": 8,
    "upload_time": 33.20797490899986,
    "total_upload_time": 84.7523144679999
  },
  {
    "engine_name": "milvus",
    "upload_time": 211.8904368180083,
    "total_upload_time": 805.1374587280006,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-filters",
    "parallel": 8,
    "p95_time": 1.1218322960980003,
    "rps": 11.869472873506725,
    "p99_time": 1.3226210009596255,
    "mean_time": 0.6723157582414598,
    "mean_precisions": 0.99765,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "upload_time": 786.3904986359994,
    "total_upload_time": 791.497461025996,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-filters",
    "parallel": 8,
    "p95_time": 0.21521003225498134,
    "rps": 89.69714523141516,
    "p99_time": 0.2744370680639987,
    "mean_time": 0.08775116350248281,
    "mean_precisions": 0.44247,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 183.96301186599885,
    "total_upload_time": 960.1803249129989,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-filters",
    "parallel": 8,
    "p95_time": 0.008454260001417423,
    "rps": 1199.5911677177578,
    "p99_time": 0.00965474700820778,
    "mean_time": 0.0065190274561959085,
    "mean_precisions": 0.91241,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "elastic",
    "upload_time": 958.4382368149963,
    "total_upload_time": 958.450433222999,
    "setup_name": "elastic-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-no-filters",
    "parallel": 8,
    "p95_time": 0.1387102062544727,
    "rps": 74.73647063060316,
    "p99_time": 0.1623315192028531,
    "mean_time": 0.10558298158119724,
    "mean_precisions": 0.62572,
    "engine_params": {
      "parallel": 8,
      "num_candidates": 128
    }
  },
  {
    "engine_name": "qdrant",
    "upload_time": 65.91457536999951,
    "total_upload_time": 110.98573015500006,
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "h-and-m-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.0036513524491965654,
    "rps": 758.2523352203556,
    "p99_time": 0.003995483000217065,
    "mean_time": 0.003233249979300308,
    "mean_precisions": 0.99816,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "upload_time": 821.4987202839984,
    "total_upload_time": 821.4987622860062,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-no-filters",
    "parallel": 8,
    "p95_time": 0.013648258440662175,
    "rps": 808.2050531985926,
    "p99_time": 0.02064537066500635,
    "mean_time": 0.009765109761140775,
    "mean_precisions": 0.9924,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 175.42912030099978,
    "total_upload_time": 175.42916640199974,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "h-and-m-2048-no-filters",
    "parallel": 8,
    "p95_time": 0.0117712394502405,
    "rps": 764.7457132787102,
    "p99_time": 0.012644969089910774,
    "mean_time": 0.01005423590510004,
    "mean_precisions": 0.9986800000000001,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 4285.521239761991,
    "total_upload_time": 4285.5212792620005,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-no-filters",
    "parallel": 8,
    "p95_time": 0.006318166994606145,
    "rps": 1412.585862917276,
    "p99_time": 0.007078137002681616,
    "mean_time": 0.005506940040709742,
    "mean_precisions": 0.99254,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.01563864300151181,
    "rps": 573.2371784236358,
    "p99_time": 0.017692109489617,
    "mean_time": 0.011756236765598078,
    "mean_precisions": 0.8986480000000001,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "h-and-m-2048-filters",
    "parallel": 8,
    "upload_time": 24.30409269899974,
    "total_upload_time": 369.89128604000143
  },
  {
    "engine_name": "qdrant",
    "p95_time": 0.004403223001281731,
    "rps": 2032.514361921886,
    "p99_time": 0.005016113001183841,
    "mean_time": 0.0038032377953910327,
    "mean_precisions": 0.9899700000000001,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "hnsw_ef": 128
      }
    },
    "setup_name": "qdrant-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-no-filters",
    "parallel": 8,
    "upload_time": 135.61498762100018,
    "total_upload_time": 491.16749738
  },
  {
    "engine_name": "milvus",
    "upload_time": 187.15349870700447,
    "total_upload_time": 593.4174981420074,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-no-filters",
    "parallel": 8,
    "p95_time": 0.04464091939153149,
    "rps": 312.53969702455674,
    "p99_time": 0.06507382202980813,
    "mean_time": 0.02411255849552399,
    "mean_precisions": 0.99365,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "p95_time": 2.9352467063014047,
    "rps": 6.0867942767604575,
    "p99_time": 3.2568878086292536,
    "mean_time": 1.3136171596057888,
    "mean_precisions": 0.99556,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-filters",
    "parallel": 8,
    "upload_time": 826.5599381060019,
    "total_upload_time": 826.5599835059984
  },
  {
    "engine_name": "weaviate",
    "upload_time": 80.04183274600655,
    "total_upload_time": 80.04187854600605,
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "h-and-m-2048-filters",
    "parallel": 8,
    "p95_time": 0.08480733054020675,
    "rps": 170.91161671588404,
    "p99_time": 0.11864908981078771,
    "mean_time": 0.04653029686248046,
    "mean_precisions": 0.9545878095238095,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "milvus",
    "upload_time": 37.37267245698604,
    "total_upload_time": 254.4448660609778,
    "setup_name": "milvus-m-16-ef-128",
    "dataset_name": "h-and-m-2048-filters",
    "parallel": 8,
    "p95_time": 0.18038830443692858,
    "rps": 66.20959856685928,
    "p99_time": 0.19856844001449647,
    "mean_time": 0.1191696237471333,
    "mean_precisions": 0.9994880000000002,
    "engine_params": {
      "parallel": 8,
      "params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "redis",
    "upload_time": 4315.254399509999,
    "total_upload_time": 4315.254449611006,
    "setup_name": "redis-m-16-ef-128",
    "dataset_name": "arxiv-titles-384-filters",
    "parallel": 8,
    "p95_time": 0.14093640055216383,
    "rps": 209.12118412840363,
    "p99_time": 0.318152676022437,
    "mean_time": 0.03801539682005969,
    "mean_precisions": 0.4971,
    "engine_params": {
      "parallel": 8,
      "search_params": {
        "ef": 128
      }
    }
  },
  {
    "engine_name": "weaviate",
    "p95_time": 0.04614587849971482,
    "rps": 249.52705714555242,
    "p99_time": 0.05504403435969381,
    "mean_time": 0.03183474185019913,
    "mean_precisions": 0.99872,
    "engine_params": {
      "parallel": 8,
      "vectorIndexConfig": {
        "ef": 128
      }
    },
    "setup_name": "weaviate-m-16-ef-128",
    "dataset_name": "h-and-m-2048-no-filters",
    "parallel": 8,
    "upload_time": 73.00220887399973,
    "total_upload_time": 73.00225017399998
  }
]
```