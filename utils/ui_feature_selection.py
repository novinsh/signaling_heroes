from ipywidgets import interact, interact_manual
import ipywidgets as widgets

# Following features concluded from the feature selection notebook
mask_init = ['gsm_map_ms_msc_Number', 'gsm_map_ms_vlr_Number', 'tcap_tid',
       'tcap_otid', 'e164_country_code', 'gsm_map_ms_imsi',
       'sccp_called_digits', 'e164_msisdn_2', 'gsm_map_ms_phase3', 'frame_len',
       'e212_imsi', 'tcap_localValue', 'tcap_application_context_name',
       'gsm_map_ss_ss_Code', 'e164_msisdn', 'gsm_old_localValue',
       'e164_country_code_2']

maskWidget = widgets.SelectMultiple(
    options=mask_init,
    value=mask_init,
    # rows=10,
    description='Features:',
    disabled=False,
)

def f(a):
    mask = a
    print('selected features applied:', mask)

interact_manual(f, a=maskWidget);