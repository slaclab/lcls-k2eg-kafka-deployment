import sys

template = """
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: {0}-{1}-reply
  labels:
    strimzi.io/cluster: lcls-cluster
spec:
  partitions: 1
  replicas: 3
  config:
    retention.ms: 7200000
    segment.bytes: 1073741824
"""

def create_topic_yaml(dest_folder, app_name, max_count_intances):
    for i in range(1, max_count_intances+1):
        with open(f"{dest_folder}/topic-{app_name}-{i}.yaml", "w") as file:
            file.write(template.format(app_name, str(i)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # sys.argv[1] will be the first parameter, sys.argv[2] the second, and so on.
        for i, param in enumerate(sys.argv[1:], start=1):
            if i == 1:
                dest_folder = param
            elif i == 2:
                app_name = param
            elif i ==3:
                max_instances = param
    else:
        exit(1)
    create_topic_yaml(dest_folder, app_name, int(max_instances))