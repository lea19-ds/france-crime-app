source ./configuration.conf

cd services/data_collector/bin
bash run.sh

cd ../../data_integrator/bin
bash run.sh

cd ../../data_processor/bin
bash run.sh

cd ../../web_app/bin
bash run.sh
