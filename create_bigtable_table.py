from google.cloud import bigtable

client = bigtable.Client(project="#PROJECT_NAME", admin=True)
instance = client.instance("#BIGTABLE_INSTANCE")


def create_bigtable_table(table_id):
    print('Creating the {} table.'.format(table_id))
    table = instance.table(table_id)
    table.create()
    column_family_id = 'event'
    cf1 = table.column_family(column_family_id)
    cf1.create()