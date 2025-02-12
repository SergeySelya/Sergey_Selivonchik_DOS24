# base on https://learn.kodekloud.com/user/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial/
Одна нода кубернетиса с несколькими контейнирами внутри - Миньён 
кластер - нескольно нод в каждой из который есть один контейнер

1. Master Node (Узел управления)
Master Node отвечает за управление кластером, координацию работы всех компонентов и управление состоянием кластера.

# Ключевые модули Kubernetes:

- kube-apiserver — API-сервер.
- kube-controller-manager — управляет контроллерами.
- kube-scheduler — назначает поды на ноды.
- kubelet — агент на каждой ноде.
- kube-proxy — управляет сетью и маршрутизацией.
- etcd — распределенная база данных.
- Cloud Controller Manager — взаимодействие с облачными провайдерами.
- CoreDNS — DNS-резолвинг в кластере.
- kubectl — инструмент для взаимодействия с кластером.
- Ingress Controller — управление внешним доступом к сервисам.

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
kubectl create deployment my-deployment --image=nginx
kubectl create namespace my-namespace

kubectl get pods --field-selector spec.nodeName=<node-name>
```

# ReplicaSet

<img width="848" alt="image" src="https://github.com/user-attachments/assets/f940dabb-0f4b-41e6-b810-74724093e55e" />

```bash
kubectl scale replicaset <name> --replicas=2

```

# deployments
```bash
kubectl create -f <name-deployment.yaml>
```

<img width="1061" alt="image" src="https://github.com/user-attachments/assets/0268f6c1-96a7-43d9-a81e-8d07ad17b0db" />

# Update and Rollback
<img width="1008" alt="image" src="https://github.com/user-attachments/assets/d74469a3-9d6e-4dee-b47c-c9e6d9ad92be" />



