#! /bin/bash

export PYTHONPATH=../src/

rm .coverage

for test_file in `ls *_tests.py`
do
    coverage run --append --source ../src/ $test_file
done

min=60
current_coverage=`coverage report -m | grep  TOTAL | awk '{print $4}' | sed s/%//g`
echo "Current coverage is $current_coverage. See more detail in htmlcov."

if [ $current_coverage -lt $min ]; then
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    echo -e "${RED}Current coverage $current_coverage is lower than min requirement $min!!! ${NC}"
    exit -1
fi

coverage html
