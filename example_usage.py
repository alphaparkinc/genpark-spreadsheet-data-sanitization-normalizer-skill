from client import SpreadsheetDataSanitizationNormalizerClient

def main():
    client = SpreadsheetDataSanitizationNormalizerClient()
    res = client.sanitize_tabular_dataset('sales_aug_dirty.csv')
    print('Data Sanitization Normalizer: ' + res['sanitization_id'])
    print('Repaired: ' + str(res['dirty_fields_repaired']) + ' fields | ISO8601: ' + str(res['date_format_unified_iso8601']))
    print('Clean CSV URL: ' + res['clean_export_url'])

if __name__ == '__main__':
    main()
