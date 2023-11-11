<h1>Lastminuteresy restaurant-integration-function</h1>

<p>
Serverless function to attempt and return potential restaurant booking from request on pub/sub topic
</p>

<h2>Run locally</h2>
<p>
pip install -r requirements.txt
TODO
</p>

<h2>Deploy process</h2>
TBA
<!-- <p>prerequisties: docker image for linux (see above) and gcloud auth / credentials configured</p>
<ul>
<li>push artifact (image) <br>
docker push europe-west1-docker.pkg.dev/${PROJECT_ID}/lastminuteresy/table-service:tag</li>
<li>(optional) credentials for cluster<br>
gcloud container clusters get-credentials hello-cluster --region europe-west1</li>
<li><strong>create deployment for new image</strong><br>
kubectl create deployment table-service --image=europe-west1-docker.pkg.dev/${PROJECT_ID}/lastminuteresy/table-service:tag</li>
<br>alternative rolling update only <br>
kubectl set image deployment/table-service table-service=europe-west1-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:new-tag
<li>set replicas (if needed)<br>
kubectl scale deployment table-service --replicas=3
<br>autoscaling (optional)<br>
kubectl autoscale deployment table-service --cpu-percent=80 --min=1 --max=5
<li>???</li>
<li>Profit</li>

</ul>
-->