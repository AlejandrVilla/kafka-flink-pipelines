from pyflink.table import TableEnvironment, EnvironmentSettings
from pyflink.table.expressions import col, concat

# Create a TableEnvironment
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

# Instrucción para eliminar la tabla
t_env.execute_sql("DROP TABLE IF EXISTS source_table")

# Specify connector and format jars
t_env.get_config().get_configuration().set_string(
    "pipeline.jars",
    "file:///usr/lib/flink/lib/flink-sql-connector-kafka-3.2.0.jar"
)

# Define source table DDL
source_ddl = """
    CREATE TABLE source_table(
        id_str VARCHAR,
        username VARCHAR,
        tweet VARCHAR,
        location VARCHAR,
        retweet_count BIGINT,
        followers_count BIGINT,
        lang VARCHAR
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'my-topic-test',
        'properties.bootstrap.servers' = 'ec2-34-226-148-69.compute-1.amazonaws.com:9092',
        'properties.group.id' = 'test_3',
        'scan.startup.mode' = 'latest-offset',
        'format' = 'json'
    )
"""

# Definir la tabla sink (HDFS)
sink_ddl_hdfs = """
    CREATE TABLE sink_table(
        id_str VARCHAR,
        username VARCHAR,
        tweet VARCHAR,
        location VARCHAR,
        retweet_count BIGINT,
        followers_count BIGINT,
        lang VARCHAR
    ) WITH (
        'connector' = 'filesystem',
        'path' = 'hdfs:///your-hdfs-path/tweets',
        'format' = 'csv'
    )
"""

# Execute DDL statement to create the source table
t_env.execute_sql(source_ddl)
t_env.execute_sql(sink_ddl_hdfs)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Process the data
result_table = source_table.select(
    col("id_str"),
    col("username"),
    col("tweet"),
    col("location"),
    col("retweet_count"),
    col("followers_count"),
    col("lang")
)

# Retrieve the sink table
sink_table = t_env.from_path('sink_table')

print("Sink Table Schema:")
sink_table.print_schema()

# Insert the processed data into the sink table
result_table.execute_insert('sink_table').wait()