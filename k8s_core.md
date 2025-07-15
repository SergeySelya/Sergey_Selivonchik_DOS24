# base on https://learn.kodekloud.com/user/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial/
Одна нода кубернетиса с несколькими контейнирами внутри - Миньён 
кластер - нескольно нод в каждой из который есть один контейнер

1. Master Node (Узел управления)
Master Node отвечает за управление кластером, координацию работы всех компонентов и управление состоянием кластера.

<img width="1048" height="778" alt="image" src="https://github.com/user-attachments/assets/ee706e9d-625a-4a93-976b-92f82b34368b" />

# Ключевые модули Kubernetes:

- kube-apiserver — коммуникация между master node и worker node.
- kube-controller-manager — контролирует все поды в рамках всего кластера.
- kube-scheduler — назначает поды на ноды , распределяет нагрузку между нодами.
- kubelet — агент на каждой ноде, для комуникации между разными подами и нодами в кластере.
- kube-proxy — управляет сетью и маршрутизацией, в рамках каждой ноды.
- etcd — распределенная база данных, хранение логов.
- Cloud Controller Manager — взаимодействие с облачными провайдерами.
- CoreDNS — DNS-резолвинг в кластере (name=ip).
- kubectl — инструмент для взаимодействия с кластером.
- Ingress Controller — управление внешним доступом к сервисам.
  
![telegram-cloud-photo-size-2-5451721793086813257-y](https://github.com/user-attachments/assets/2119c4c3-a0f0-44a7-9813-69b3c8618b3b)

```bash
# кол-во нод
kubectl get nodes
#информация о нодах
kubectl get nodes -o wide
# статус ключевых компонентов кластера, таких как scheduler, controller-manager и etcd:
kubectl get componentstatuses

# создание пода
kubectl run nginx --image=nginx
# инфо о поде
kubectl describe pod <name>
kubectl get pods 
kubectl get nodes -o wide
# создание пода с помощью yaml файла
kubectl create -f pod-definitions.yaml
kubectl apply -f pod-definitions.yaml
# посмотреть эти деплойменты
kubectl get deployments
#редактировать деплойменты
kubectl edit deployment <deployment-name>
```
<img width="905" alt="image" src="https://github.com/user-attachments/assets/dd3ac716-6433-4ccb-8d52-aed31771cce9" />
```bash
# удаление пода
kubectl delete pod <name>
# редактирование конфигурации пода
kubectl edit pod
# или изменить yaml файл и сделать следующую команды:
kubectl apply -f config.yml
kubectl create pod my-pod --image=nginx

# Deployment
kubectl create deployment my-deployment --image=nginx
kubectl create namespace my-namespace
kubectl scale deployment my-deployment --replicas=3

# Services (TYPE: ClusterIP, NodePort, LoadBalancer)
kubectl expose deployment my-deployment --type=LoadBalancer --port=8080 --targetp-port=80
kubectl get services

| Тип сервиса      | Доступ откуда?           | Внешний IP?      | Описание                                                                   |
| ---------------- | ------------------------ | ---------------- | -------------------------------------------------------------------------- |
| **ClusterIP**    | Только внутри кластера   | ❌ Нет            | По умолчанию. Используется для связи между подами внутри кластера.         |
| **NodePort**     | Извне через порт на узле | ⚠️ Через IP ноды | Открывает порт на каждом узле (ноде), доступ снаружи через `<NodeIP>:Port` |
| **LoadBalancer** | Из интернета             | ✅ Да             | Создаёт внешний балансировщик (в облаке), трафик идёт на нужный под        |

```

# ReplicaSet

<img width="848" alt="image" src="https://github.com/user-attachments/assets/f940dabb-0f4b-41e6-b810-74724093e55e" />

```bash
# Replicaset - контролирует поды
# Replica - пода
kubectl scale replicaset <name> --replicas=2


```

# deployments 
```bash
# deployments - обькт который управляет развертыванием имен и обновлением экземпляров приложения

kubectl create -f <name-deployment.yaml>
kubectl create deployment my-deployment --image=nginx
kubectl create namespace my-namespace
kubectl scale deployment my-deployment --replicas=3
```

<img width="1061" alt="image" src="https://github.com/user-attachments/assets/0268f6c1-96a7-43d9-a81e-8d07ad17b0db" />

# Update and Rollback
<img width="1008" alt="image" src="https://github.com/user-attachments/assets/d74469a3-9d6e-4dee-b47c-c9e6d9ad92be" />



