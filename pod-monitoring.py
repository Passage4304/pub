from kubernetes import client, config

def monitor_pods():
    """
    Мониторит поды в Kubernetes кластере, выводя информацию о них.
    """
    try:
        config.load_kube_config()
    except Exception as e:
        print(f"Ошибка загрузки конфигурации Kubernetes: {e}")
        return

    v1 = client.CoreV1Api()

    try:
        ret = v1.list_namespaced_pod(namespace="default")
        for i in ret.items:
            pod_name = i.metadata.name
            pod_status = i.status.phase
            node_name = i.spec.node_name
            print(f"Под: {pod_name}, Статус: {pod_status}, Узел: {node_name}")

    except client.ApiException as e:
        print(f"Ошибка при получении списка подов: {e}")

if __name__ == "__main__":
    monitor_pods()