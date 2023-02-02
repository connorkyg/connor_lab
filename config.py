import requests
import inspect

server_protocol = 'https://'
server_domain = '192.168.199.161'
api_ver = '/api/v1'
api_base_url = f'https://{server_domain}/api/v1'


header = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': f'https://{server_domain}/setting/system/login',
    'sec-ch-ua': '\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin'
}



# Login -> Token 발급
def post_Login():
    api_name = '/Login'
    apiUrl = api_base_url + api_name
    userId = 'ssrca'
    userPasswd = 'qwe123qwe123!'
    data = {
        "userId": userId,
        "userPasswd": userPasswd,
        "saveId": 0
    }
    header = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://' + server_domain + '/setting/system/login',
        'sec-ch-ua': '\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\"Windows\"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    response = requests.post(url=apiUrl, headers=header, json=data, verify=False)
    cookie = response.headers['Set-Cookie']

    return response, cookie


def get_AdminAccountPolicy(headers):
    response = requests.get(f'{api_base_url}/Admin/AccountPolicy', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminCommonSetting(headers):
    response = requests.get(f'{api_base_url}/Admin/CommonSetting', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminDBBackUpSetting(headers):
    response = requests.get(f'{api_base_url}/Admin/DBBackUpSetting', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminLicense(headers):
    response = requests.get(f'{api_base_url}/Admin/License', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminPatternSetting(headers):
    response = requests.get(f'{api_base_url}/Admin/PatternSetting', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminPatternSettingCVEManual(headers):
    version = 'CVE-583-13-245-20221215'
    params = {
        'version': version
    }
    response = requests.get(f'{api_base_url}/Admin/PatternSetting/CVE/Manual', headers=headers, params=params, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminPatternSettingCVEOnline(headers):
    response = requests.get(f'{api_base_url}/Admin/PatternSetting/CVE/Online', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminPatternSettingCollectManual(headers):
    version = 'COLLECT-31-2-2-0-20221209'
    params = {
        'version': version
    }
    response = requests.get(f'{api_base_url}/Admin/PatternSetting/Collect/Manual', headers=headers, params=params, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminPatternSettingCollectOnline(headers):
    response = requests.get(f'{api_base_url}/Admin/PatternSetting/Collect/Online', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminUser(headers):
    response = requests.get(f'{api_base_url}/Admin/User', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AdminUserCheckCount(headers):
    response = requests.get(f'{api_base_url}/Admin/User/CheckCount', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AgentDownload(headers):
    os_list = ['windows', 'linux', 'solaris', 'hpux', 'aix', 'network']
    for i in range(len(os_list)):
        os = os_list[i]
        params = {
            'os': os
        }
        try:
            response = requests.get(f'{api_base_url}/Agent/Download', headers=headers, params=params, verify=False)
            if response.status_code == 200:
                pass
            else:
                print(f'[FAIL] {inspect.currentframe().f_code.co_name}: {response}')
                print(f'{response.text}')
                print('\n')
        except requests.exceptions as e:
            print(f'[ERROR] {inspect.currentframe().f_code.co_name}: {e}')
            print('\n')
        print(f'[OKAY] {inspect.currentframe().f_code.co_name}')
    return response


def get_AgentDownloadManualGuide(headers):
    response = requests.get(f'{api_base_url}/Agent/Download/ManualGuide', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AgentVersion(headers):
    response = requests.get(f'{api_base_url}/Agent/Version', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_Asset(headers):
    response = requests.get(f'{api_base_url}/Asset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetManage(headers):
    response = requests.get(f'{api_base_url}/Asset/Manage', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetNoGroupAsset(headers):
    response = requests.get(f'{api_base_url}/Asset/NoGroupAsset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetOsType(headers):
    response = requests.get(f'{api_base_url}/Asset/OsType', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroup(headers):
    response = requests.get(f'{api_base_url}/AssetGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupChildGroupCount(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/ChildGroup/Count', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupChildGroupSummery(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/ChildGroup/Summery', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupConnectionGroup(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/ConnectionGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManage(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManageAssetRegistered(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage/Asset/Registered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManageAssetUnregistered(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage/Asset/Unregistered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManageAssetGroup(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage/AssetGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManageUserGroupRegistered(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage/UserGroup/Registered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetGroupManageUserGroupUnregistered(headers):
    response = requests.get(f'{api_base_url}/AssetGroup/Manage/UserGroup/Unregistered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatus(headers):
    response = requests.get(f'{api_base_url}/AssetStatus', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatusAssetSummary(headers):
    response = requests.get(f'{api_base_url}/AssetStatus/AssetSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatusHardwareDetail(headers):
    response = requests.get(f'{api_base_url}/AssetStatus/HardwareDetail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatusPortDetail(headers):
    params = {
        'offset': 1,
        'limit': 1,
        'aiNo': 1,
        'assetGroupFilter': 1,
        'assetFilter': 1,
        'filter': 1,
        'order': 1
    }
    response = requests.get(f'{api_base_url}/AssetStatus/PortDetail', headers=headers, params=params, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatusProductDetail(headers):
    response = requests.get(f'{api_base_url}/AssetStatus/ProductDetail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_AssetStatusServiceDetail(headers):
    response = requests.get(f'{api_base_url}/AssetStatus/ServiceDetail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_CVE(headers):
    response = requests.get(f'{api_base_url}/CVE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_CveAssetList(headers):
    response = requests.get(f'{api_base_url}/Cve/AssetList', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_CveDetail(headers):
    response = requests.get(f'{api_base_url}/Cve/Detail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamCVE(headers):
    response = requests.get(f'{api_base_url}/Exam/CVE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamExamNameCheck(headers):
    response = requests.get(f'{api_base_url}/Exam/Exam/NameCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamExamAssetSummary(headers):
    response = requests.get(f'{api_base_url}/Exam/ExamAssetSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamHistory(headers):
    response = requests.get(f'{api_base_url}/Exam/History', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamHistoryDetail(headers):
    response = requests.get(f'{api_base_url}/Exam/History/Detail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamHistoryDetailExamAssetSummary(headers):
    response = requests.get(f'{api_base_url}/Exam/History/Detail/ExamAssetSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManual(headers):
    response = requests.get(f'{api_base_url}/Exam/Manual', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManualDetail(headers):
    response = requests.get(f'{api_base_url}/Exam/Manual/Detail', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManualDetailAsset(headers):
    response = requests.get(f'{api_base_url}/Exam/Manual/Detail/Asset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManualDetailConfirm(headers):
    response = requests.get(f'{api_base_url}/Exam/Manual/Detail/Confirm', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManualNameCheck(headers):
    response = requests.get(f'{api_base_url}/Exam/Manual/NameCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamManualInterlockSummary(headers):
    response = requests.get(f'{api_base_url}/Exam/ManualInterlockSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamProduct(headers):
    response = requests.get(f'{api_base_url}/Exam/Product', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamReservation(headers):
    response = requests.get(f'{api_base_url}/Exam/Reservation', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamReservationNameCheck(headers):
    response = requests.get(f'{api_base_url}/Exam/Reservation/NameCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamTemplateCPE(headers):
    response = requests.get(f'{api_base_url}/Exam/Template/CPE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ExamTemplateCVE(headers):
    response = requests.get(f'{api_base_url}/Exam/Template/CVE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InterlockSolidStep(headers):
    response = requests.get(f'{api_base_url}/Interlock/SolidStep', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InterlockSolidStepAsset(headers):
    response = requests.get(f'{api_base_url}/Interlock/SolidStepAsset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryInventoryDetailCve(headers):
    response = requests.get(f'{api_base_url}/Inventory/InventoryDetailCve', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryManualCPEProductCheck(headers):
    response = requests.get(f'{api_base_url}/Inventory/Manual/CPE/ProductCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryManualCPEVendorCheck(headers):
    response = requests.get(f'{api_base_url}/Inventory/Manual/CPE/VendorCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryPort(headers):
    response = requests.get(f'{api_base_url}/Inventory/Port', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryPortDetailAsset(headers):
    response = requests.get(f'{api_base_url}/Inventory/PortDetailAsset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryProduct(headers):
    response = requests.get(f'{api_base_url}/Inventory/Product', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryProductHistory(headers):
    response = requests.get(f'{api_base_url}/Inventory/Product/History', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryProductID(headers):
    response = requests.get(f'{api_base_url}/Inventory/Product/ID', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryProductDetailAsset(headers):
    response = requests.get(f'{api_base_url}/Inventory/ProductDetailAsset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryProductSummary(headers):
    response = requests.get(f'{api_base_url}/Inventory/ProductSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryService(headers):
    response = requests.get(f'{api_base_url}/Inventory/Service', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_InventoryServiceDetailAsset(headers):
    response = requests.get(f'{api_base_url}/Inventory/ServiceDetailAsset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_LogAccess(headers):
    response = requests.get(f'{api_base_url}/Log/Access', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_LogLogin(headers):
    response = requests.get(f'{api_base_url}/Log/Login', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_LogPatch(headers):
    response = requests.get(f'{api_base_url}/Log/Patch', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_LogSystem(headers):
    response = requests.get(f'{api_base_url}/Log/System', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanApprovalCheckCountSummary(headers):
    response = requests.get(f'{api_base_url}/Plan/ApprovalCheckCountSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanAsset(headers):
    response = requests.get(f'{api_base_url}/Plan/Asset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanAssetApproval(headers):
    response = requests.get(f'{api_base_url}/Plan/AssetApproval', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanAssetBatchRegistrationSummary(headers):
    response = requests.get(f'{api_base_url}/Plan/AssetBatchRegistrationSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanAssetCheckCountSummary(headers):
    response = requests.get(f'{api_base_url}/Plan/AssetCheckCountSummary', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanAssetHistory(headers):
    response = requests.get(f'{api_base_url}/Plan/AssetHistory', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_PlanUser(headers):
    response = requests.get(f'{api_base_url}/Plan/User', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_Report(headers):
    response = requests.get(f'{api_base_url}/Report', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ReportAsset(headers):
    response = requests.get(f'{api_base_url}/Report/Asset', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ReportAssetDetailCPE(headers):
    response = requests.get(f'{api_base_url}/Report/AssetDetailCPE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ReportAssetDetailCVE(headers):
    response = requests.get(f'{api_base_url}/Report/AssetDetailCVE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ReportAssetGroup(headers):
    response = requests.get(f'{api_base_url}/Report/AssetGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_ReportReportNameCheck(headers):
    response = requests.get(f'{api_base_url}/Report/Report/NameCheck', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_SearchFindProduct(headers):
    response = requests.get(f'{api_base_url}/Search/Find/Product', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_SearchFindVendor(headers):
    response = requests.get(f'{api_base_url}/Search/Find/Vendor', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_SystemConfig(headers):
    response = requests.get(f'{api_base_url}/System/Config', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_SystemTitle(headers):
    response = requests.get(f'{api_base_url}/System/Title', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_SystemVersion(headers):
    response = requests.get(f'{api_base_url}/System/Version', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_Template(headers):
    response = requests.get(f'{api_base_url}/Template', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TemplateCPEItemRegistered(headers):
    response = requests.get(f'{api_base_url}/Template/CPE/Item/Registered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TemplateCPEItemUnRegistered(headers):
    response = requests.get(f'{api_base_url}/Template/CPE/Item/UnRegistered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TemplateCVE(headers):
    response = requests.get(f'{api_base_url}/Template/CVE', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TemplateCVEItemRegistered(headers):
    response = requests.get(f'{api_base_url}/Template/CVE/Item/Registered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TemplateCVEItemUnregistered(headers):
    response = requests.get(f'{api_base_url}/Template/CVE/Item/Unregistered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_TokenUnlimited(headers):
    response = requests.get(f'{api_base_url}/Token/Unlimited', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserAssetGroup(headers):
    response = requests.get(f'{api_base_url}/User/AssetGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserMy(headers):
    response = requests.get(f'{api_base_url}/User/My', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserUserGroup(headers):
    response = requests.get(f'{api_base_url}/User/UserGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserGroup(headers):
    response = requests.get(f'{api_base_url}/UserGroup', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserGroupManage(headers):
    response = requests.get(f'{api_base_url}/UserGroup/Manage', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserGroupManageUserRegistered(headers):
    response = requests.get(f'{api_base_url}/UserGroup/Manage/User/Registered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response


def get_UserGroupManageUserUnregistered(headers):
    response = requests.get(f'{api_base_url}/UserGroup/Manage/User/Unregistered', headers=headers, verify=False)
    print(inspect.currentframe().f_code.co_name)
    print(response)
    return response