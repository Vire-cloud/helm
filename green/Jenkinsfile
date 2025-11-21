pipeline {
    agent any

    environment {
        IMAGE_TAG = "v${BUILD_NUMBER}"
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
                gcloud auth configure-docker asia-south1-docker.pkg.dev -q
                docker build -t ${Repository}/$IMAGE_NAME:$IMAGE_TAG .
                docker push ${Repository}/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh '''
                helm upgrade --install $HELM_RELEASE $CHART_PATH -f $CHART_PATH/values.yaml \
                    --set image.repository=${Repository}/$IMAGE_NAME \
                    --set image.tag=$IMAGE_TAG \
                    --wait --timeout 1m
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Verifying resources..."
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }
}
