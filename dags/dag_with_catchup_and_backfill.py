from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'by_ect',
    'retries':5,
    'retry_delay':timedelta(seconds=20),
}


with DAG(
    default_args=default_args,
    dag_id='dag_with_catchup_and_backfill',
    description='my first dag with catchup and backfill',
    start_date=datetime(2026,2,9),
    schedule='0 0 * * *'
) as dag:
    task_set_name = BashOperator( 
        task_id='task_set_name',
        bash_command='echo "ECT"'
    )

task_set_name

"""
(dakika) (saat) (ayın günü) (ay) (haftanın günü)

1) Saat/dakika ayarlamak
	•	30 6 * * * → her gün 06:30
	•	0 * * * * → her saat başı
	•	*/15 * * * * → 15 dakikada bir
	•	0 */2 * * * → 2 saatte bir (00:00, 02:00, 04:00…)

2) Haftanın günleri

Haftanın günü alanı: 0-6 (çoğu sistemde 0=Pazar) ya da SUN,MON,...
	•	0 9 * * 1-5 → Hafta içi her gün 09:00
	•	0 10 * * 6,0 → Cumartesi+Pazar 10:00
	•	0 8 * * MON → her Pazartesi 08:00

3) Ayın günleri
	•	0 0 1 * * → her ayın 1’i 00:00
	•	0 0 15 * * → her ayın 15’i
	•	0 0 1,15 * * → her ayın 1’i ve 15’i

4) Ay seçmek
	•	0 0 * 1 * → Ocak ayı boyunca her gün 00:00
	•	0 0 1 1 * → her yıl 1 Ocak 00:00
	•	0 0 * */3 * → 3 ayda bir (Ocak/Nisan/Temmuz/Ekim) her gün 00:00

"""