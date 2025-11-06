pipeline {
    agent any

    environment {
        PROJECT_ID = "s-0-009988"
        CLUSTER_NAME = "gitlab-gke"
        CLUSTER_ZONE = "asia-south1-c"
        HELM_RELEASE = "my-nginx"
        CHART_PATH = "nginx"
        IMAGE_NAME = "nginx-test"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vire-cloud/helm.git'
            }
        }

        stage('Authenticate to GCP') {
            steps {
                withCredentials([file(credentialsId: 'service-account', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                    gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                    gcloud config set project $PROJECT_ID
                    gcloud container clusters get-credentials $CLUSTER_NAME --zone $CLUSTER_ZONE --project $PROJECT_ID
                    '''
                }
            }
        }

        stage('build and push') {
            steps {
                sh '''
                docker build -t ${Repository}/$IMAGE_NAME:$IMAGE_TAG .
                docker push ${Repository}/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh '''
                helm upgrade --install $HELM_RELEASE $CHART_PATH -f $CHART_PATH/values.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }
}
