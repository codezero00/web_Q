urlpatterns = [

    ('helloworld', 'GET', '/', 'app.helloworld'),



    # I U
    #('FRONTBASE_InsOrUp', 'POST', '/api/v1/FRONTBASE_InsOrUp', 'view_insorup.FRONTBASE_InsOrUp'),
    ('BLOODEDGE_InsOrUp', 'POST', '/api/v1/BLOODEDGE_InsOrUp', 'view_insorup.BLOODEDGE_InsOrUp'),
    ('DATALAYER_InsOrUp', 'POST', '/api/v1/DATALAYER_InsOrUp', 'view_insorup.DATALAYER_InsOrUp'),
    ('DBTABLE_InsOrUp', 'POST', '/api/v1/DBTABLE_InsOrUp', 'view_insorup.DBTABLE_InsOrUp'),
    ('DBTABLE_RELATION_InsOrUp', 'POST', '/api/v1/DBTABLE_RELATION_InsOrUp', 'view_insorup.DBTABLE_RELATION_InsOrUp'),
    ('DBTABLECOLUMN_InsOrUp', 'POST', '/api/v1/DBTABLECOLUMN_InsOrUp', 'view_insorup.DBTABLECOLUMN_InsOrUp'),
    ('FRONTBASE_InsOrUp', 'POST', '/api/v1/FRONTBASE_InsOrUp', 'view_insorup.FRONTBASE_InsOrUp'),
    ('IC_JOB_InsOrUp', 'POST', '/api/v1/IC_JOB_InsOrUp', 'view_insorup.IC_JOB_InsOrUp'),
    ('IC_RESOURCE_InsOrUp', 'POST', '/api/v1/IC_RESOURCE_InsOrUp', 'view_insorup.IC_RESOURCE_InsOrUp'),
    ('IC_RESOURCE_GROUP_InsOrUp', 'POST', '/api/v1/IC_RESOURCE_GROUP_InsOrUp', 'view_insorup.IC_RESOURCE_GROUP_InsOrUp'),
    ('IC_SOURCE_DATABASE_InsOrUp', 'POST', '/api/v1/IC_SOURCE_DATABASE_InsOrUp', 'view_insorup.IC_SOURCE_DATABASE_InsOrUp'),
    ('IC_SOURCE_DATABASE_TABLE_InsOrUp', 'POST', '/api/v1/IC_SOURCE_DATABASE_TABLE_InsOrUp', 'view_insorup.IC_SOURCE_DATABASE_TABLE_InsOrUp'),
    ('IC_SOURCE_DATABASE_TABLE_COLUMN_InsOrUp', 'POST', '/api/v1/IC_SOURCE_DATABASE_TABLE_COLUMN_InsOrUp', 'view_insorup.IC_SOURCE_DATABASE_TABLE_COLUMN_InsOrUp'),
    ('METADATA_InsOrUp', 'POST', '/api/v1/METADATA_InsOrUp', 'view_insorup.METADATA_InsOrUp'),
    ('METADATACLASS_InsOrUp', 'POST', '/api/v1/METADATACLASS_InsOrUp', 'view_insorup.METADATACLASS_InsOrUp'),
    ('NOSQLBASE_InsOrUp', 'POST', '/api/v1/NOSQLBASE_InsOrUp', 'view_insorup.NOSQLBASE_InsOrUp'),
    ('RESOURCEBASE_InsOrUp', 'POST', '/api/v1/RESOURCEBASE_InsOrUp', 'view_insorup.RESOURCEBASE_InsOrUp'),
    ('SC_APPLICATION_RECORD_InsOrUp', 'POST', '/api/v1/SC_APPLICATION_RECORD_InsOrUp', 'view_insorup.SC_APPLICATION_RECORD_InsOrUp'),
    ('SC_GROUP_InsOrUp', 'POST', '/api/v1/SC_GROUP_InsOrUp', 'view_insorup.SC_GROUP_InsOrUp'),
    ('SC_LOG_InsOrUp', 'POST', '/api/v1/SC_LOG_InsOrUp', 'view_insorup.SC_LOG_InsOrUp'),
    ('SC_SERVICE_InsOrUp', 'POST', '/api/v1/SC_SERVICE_InsOrUp', 'view_insorup.SC_SERVICE_InsOrUp'),
    ('SC_SERVICE_REQUEST_PARAMETERS_InsOrUp', 'POST', '/api/v1/SC_SERVICE_REQUEST_PARAMETERS_InsOrUp', 'view_insorup.SC_SERVICE_REQUEST_PARAMETERS_InsOrUp'),
    ('USERS_InsOrUp', 'POST', '/api/v1/USERS_InsOrUp', 'view_insorup.USERS_InsOrUp'),
    

    # BabchDel
    #('BLOODEDGE_BatchDel', 'POST', '/api/v1/BLOODEDGE_BatchDel', 'view_del.BLOODEDGE_BatchDel'),
    ('BLOODEDGE_BatchDel', 'POST', '/api/v1/BLOODEDGE_BatchDel', 'view_del.BLOODEDGE_BatchDel'),
    ('DATALAYER_BatchDel', 'POST', '/api/v1/DATALAYER_BatchDel', 'view_del.DATALAYER_BatchDel'),
    ('DBTABLE_BatchDel', 'POST', '/api/v1/DBTABLE_BatchDel', 'view_del.DBTABLE_BatchDel'),
    ('DBTABLE_RELATION_BatchDel', 'POST', '/api/v1/DBTABLE_RELATION_BatchDel', 'view_del.DBTABLE_RELATION_BatchDel'),
    ('DBTABLECOLUMN_BatchDel', 'POST', '/api/v1/DBTABLECOLUMN_BatchDel', 'view_del.DBTABLECOLUMN_BatchDel'),
    ('FRONTBASE_BatchDel', 'POST', '/api/v1/FRONTBASE_BatchDel', 'view_del.FRONTBASE_BatchDel'),
    ('IC_JOB_BatchDel', 'POST', '/api/v1/IC_JOB_BatchDel', 'view_del.IC_JOB_BatchDel'),
    ('IC_RESOURCE_BatchDel', 'POST', '/api/v1/IC_RESOURCE_BatchDel', 'view_del.IC_RESOURCE_BatchDel'),
    ('IC_RESOURCE_GROUP_BatchDel', 'POST', '/api/v1/IC_RESOURCE_GROUP_BatchDel', 'view_del.IC_RESOURCE_GROUP_BatchDel'),
    ('IC_SOURCE_DATABASE_BatchDel', 'POST', '/api/v1/IC_SOURCE_DATABASE_BatchDel', 'view_del.IC_SOURCE_DATABASE_BatchDel'),
    ('IC_SOURCE_DATABASE_TABLE_BatchDel', 'POST', '/api/v1/IC_SOURCE_DATABASE_TABLE_BatchDel', 'view_del.IC_SOURCE_DATABASE_TABLE_BatchDel'),
    ('IC_SOURCE_DATABASE_TABLE_COLUMN_BatchDel', 'POST', '/api/v1/IC_SOURCE_DATABASE_TABLE_COLUMN_BatchDel', 'view_del.IC_SOURCE_DATABASE_TABLE_COLUMN_BatchDel'),
    ('METADATA_BatchDel', 'POST', '/api/v1/METADATA_BatchDel', 'view_del.METADATA_BatchDel'),
    ('METADATACLASS_BatchDel', 'POST', '/api/v1/METADATACLASS_BatchDel', 'view_del.METADATACLASS_BatchDel'),
    ('NOSQLBASE_BatchDel', 'POST', '/api/v1/NOSQLBASE_BatchDel', 'view_del.NOSQLBASE_BatchDel'),
    ('RESOURCEBASE_BatchDel', 'POST', '/api/v1/RESOURCEBASE_BatchDel', 'view_del.RESOURCEBASE_BatchDel'),
    ('SC_APPLICATION_RECORD_BatchDel', 'POST', '/api/v1/SC_APPLICATION_RECORD_BatchDel', 'view_del.SC_APPLICATION_RECORD_BatchDel'),
    ('SC_GROUP_BatchDel', 'POST', '/api/v1/SC_GROUP_BatchDel', 'view_del.SC_GROUP_BatchDel'),
    ('SC_LOG_BatchDel', 'POST', '/api/v1/SC_LOG_BatchDel', 'view_del.SC_LOG_BatchDel'),
    ('SC_SERVICE_BatchDel', 'POST', '/api/v1/SC_SERVICE_BatchDel', 'view_del.SC_SERVICE_BatchDel'),
    ('SC_SERVICE_REQUEST_PARAMETERS_BatchDel', 'POST', '/api/v1/SC_SERVICE_REQUEST_PARAMETERS_BatchDel', 'view_del.SC_SERVICE_REQUEST_PARAMETERS_BatchDel'),
    ('USERS_BatchDel', 'POST', '/api/v1/USERS_BatchDel', 'view_del.USERS_BatchDel'),
    

]