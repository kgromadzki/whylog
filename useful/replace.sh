#!/bin/bash
find ../ -name "parsers.yaml" -print0 | xargs -0 sed -i 's/---/---\nclass: RegexParser\nlog_type : default/g'
find ../ -name "rules*.yaml" -print0 | xargs -0 sed -i 's/cause: \([a-z]*\)/causes: [\1]/g'
echo -e "---\n['RegexParser', {'type': 'default', 'path_pattern': 'node_1.log'}]" > log_locations.yaml
for i in $( find ../whylog/ -name "[0-9]*" -type d); do
    cp log_locations.yaml $i
done
rm log_locations.yaml