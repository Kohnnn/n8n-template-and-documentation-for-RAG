---
url: "https://qdrant.tech/articles_data/io_uring/rescore-benchmark.sh"
title: undefined
---

#!/bin/bash
export QDRANT\_URL=""
export COLLECTION=""
export CONCURRENCY=4 # or 8
export OVERSAMPLING=1 # or 4

time seq 1000 \| xargs -P ${CONCURRENCY} -I {} curl -L -X POST \
 "http://${QDRANT\_URL}/collections/${COLLECTION}/points/recommend" \
 -H 'Content-Type: application/json' --data-raw \
 "{ \\"limit\\": 10, \\"positive\\": \[{}\], \\"params\\": { \\"quantization\\": \
 { \\"rescore\\": true, \\"oversampling\\": ${OVERSAMPLING} } } }" \
 -s \| jq .status \| wc -l

time seq 1000 2000 \| xargs -P ${CONCURRENCY} -I {} curl -L -X POST \
 "${QDRANT\_URL}/collections/${COLLECTION}/points/recommend" \
 -H 'Content-Type: application/json' --data-raw \
 "{ \\"limit\\": 10, \\"positive\\": \[{}\], \\"params\\": { \\"quantization\\": \
 { \\"rescore\\": true, \\"oversampling\\": ${OVERSAMPLING} } } }" \
 -s \| jq .status \| wc -l

time seq 2000 3000 \| xargs -P ${CONCURRENCY} -I {} curl -L -X POST \
 "${QDRANT\_URL}/collections/${COLLECTION}/points/recommend" \
 -H 'Content-Type: application/json' --data-raw \
 "{ \\"limit\\": 10, \\"positive\\": \[{}\], \\"params\\": { \\"quantization\\": \
 { \\"rescore\\": true, \\"oversampling\\": ${OVERSAMPLING} } } }" \
 -s \| jq .status \| wc -l