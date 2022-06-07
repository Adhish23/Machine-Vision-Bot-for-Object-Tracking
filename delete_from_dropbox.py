import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


dbx = dropbox.Dropbox('oG7g0mYYCfAAAAAAAAAAD71siPToPbfzNVclK-9lY-jDzYahVep2AGKFXymw8jC3'):
print('Deleting current file....')
dbx.files_delete('/frozen_inference_graph.txt')
print('Sucessfully deleted !')
