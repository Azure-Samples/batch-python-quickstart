#-------------------------------------------------------------------------
# 
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
#----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
#--------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "

_AUTH_MODE = 'Key' # VALUE SHOULD BE 'Key' OR 'ServicePrincipal'
_BATCH_ACCOUNT_NAME ='' # Your batch account name 
_BATCH_ACCOUNT_KEY = '' # Your batch account key, only used for 'Key' _AUTH_MODE
_BATCH_ACCOUNT_URL = '' # Your batch account URL
_AD_CLIENT_ID = '' # Your Active Directory CLIENT_ID, only used for 'ServicePrincipal' _AUTH_MODE
_AD_TENANT = '' # Your Active Directory TENANT, only used for 'ServicePrincipal' _AUTH_MODE
_AD_SECRET = '' # Your Active Directory SECRET, only used for 'ServicePrincipal' _AUTH_MODE
_STORAGE_ACCOUNT_NAME = '' # Your storage account name
_STORAGE_ACCOUNT_KEY = '' # Your storage account key
_POOL_ID = 'PythonQuickstartPool' # Your Pool ID
_POOL_NODE_COUNT = 2 # Pool node count
_POOL_VM_SIZE = 'STANDARD_A1_v2' # VM Type/Size
_JOB_ID = 'PythonQuickstartJob' # Job ID
_STANDARD_OUT_FILE_NAME = 'stdout.txt' # Standard Output file