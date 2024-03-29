import lists
import config
import urllib3
# see if it words
# make second history
# make third history
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

server_domain = config.server_domain

if __name__ == '__main__':
    # login -> Header 내 Cookie에 Token값 세팅
    response, cookie = config.post_Login()
    # todo: header 내 Cookie 값만 업데이트하도록... 단, key 값의 이름도 세팅해야함 (Cookie: asdasdasd~~)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookie,
        'referer': f'https://{server_domain}/setting/system/login',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\"Windows\"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }

    # comment: get apis
    # config.get_AdminAccountPolicy(headers)
    # config.get_AdminCommonSetting(headers)
    # config.get_AdminDBBackUpSetting(headers)
    # config.get_AdminLicense(headers)
    # config.get_AdminPatternSetting(headers)
    # config.get_AdminPatternSettingCVEOnline(headers)
    # config.get_AdminPatternSettingCollectOnline(headers)
    # config.get_AdminUser(headers)
    # config.get_AdminUserCheckCount(headers)
    # config.get_AgentDownloadManualGuide(headers)
    # config.get_AgentVersion(headers)
    # config.get_Asset(headers)
    # config.get_AssetManage(headers)
    # config.get_AssetNoGroupAsset(headers)
    # config.get_AssetOsType(headers)
    # config.get_AssetGroup(headers)
    # config.get_AssetGroupConnectionGroup(headers)
    # config.get_AssetGroupManage(headers)
    # config.get_AssetStatusHardwareDetail(headers)

    # comment: get apis that need parameters
    # config.get_AdminPatternSettingCVEManual(headers)
    # config.get_AdminPatternSettingCollectManual(headers)
    config.get_AgentDownload(headers) # todo: coded
    # config.get_AssetGroupChildGroupCount(headers)
    # config.get_AssetGroupChildGroupSummery(headers)
    # config.get_AssetGroupManageAssetRegistered(headers)
    # config.get_AssetGroupManageAssetUnregistered(headers)
    # config.get_AssetGroupManageAssetGroup(headers)
    # config.get_AssetGroupManageUserGroupRegistered(headers)
    # config.get_AssetGroupManageUserGroupUnregistered(headers)
    # config.get_AssetStatus(headers)
    # config.get_AssetStatusAssetSummary(headers)
    config.get_AssetStatusPortDetail(headers) # todo: coded

    # comment: apis that need to be developed
    # config.get_AssetStatusProductDetail(headers)
    # config.get_AssetStatusServiceDetail(headers)
    # config.get_CVE(headers)
    # config.get_CveAssetList(headers)
    # config.get_CveDetail(headers)
    # config.get_ExamCVE(headers)
    # config.get_ExamExamNameCheck(headers)
    # config.get_ExamExamAssetSummary(headers)
    # config.get_ExamHistory(headers)
    # config.get_ExamHistoryDetail(headers)
    # config.get_ExamHistoryDetailExamAssetSummary(headers)
    # config.get_ExamManual(headers)
    # config.get_ExamManualDetail(headers)
    # config.get_ExamManualDetailAsset(headers)
    # config.get_ExamManualDetailConfirm(headers)
    # config.get_ExamManualNameCheck(headers)
    # config.get_ExamManualInterlockSummary(headers)
    # config.get_ExamProduct(headers)
    # config.get_ExamReservation(headers)
    # config.get_ExamReservationNameCheck(headers)
    # config.get_ExamTemplateCPE(headers)
    # config.get_ExamTemplateCVE(headers)
    # config.get_InterlockSolidStep(headers)
    # config.get_InterlockSolidStepAsset(headers)
    # config.get_InventoryInventoryDetailCve(headers)
    # config.get_InventoryManualCPEProductCheck(headers)
    # config.get_InventoryManualCPEVendorCheck(headers)
    # config.get_InventoryPort(headers)
    # config.get_InventoryPortDetailAsset(headers)
    # config.get_InventoryProduct(headers)
    # config.get_InventoryProductHistory(headers)
    # config.get_InventoryProductID(headers)
    # config.get_InventoryProductDetailAsset(headers)
    # config.get_InventoryProductSummary(headers)
    # config.get_InventoryService(headers)
    # config.get_InventoryServiceDetailAsset(headers)
    # config.get_LogAccess(headers)
    # config.get_LogLogin(headers)
    # config.get_LogPatch(headers)
    # config.get_LogSystem(headers)
    # config.get_PlanApprovalCheckCountSummary(headers)
    # config.get_PlanAsset(headers)
    # config.get_PlanAssetApproval(headers)
    # config.get_PlanAssetBatchRegistrationSummary(headers)
    # config.get_PlanAssetCheckCountSummary(headers)
    # config.get_PlanAssetHistory(headers)
    # config.get_PlanUser(headers)
    # config.get_Report(headers)
    # config.get_ReportAsset(headers)
    # config.get_ReportAssetDetailCPE(headers)
    # config.get_ReportAssetDetailCVE(headers)
    # config.get_ReportAssetGroup(headers)
    # config.get_ReportReportNameCheck(headers)
    # config.get_SearchFindProduct(headers)
    # config.get_SearchFindVendor(headers)
    # config.get_SystemConfig(headers)
    # config.get_SystemTitle(headers)
    # config.get_SystemVersion(headers)
    # config.get_Template(headers)
    # config.get_TemplateCPEItemRegistered(headers)
    # config.get_TemplateCPEItemUnRegistered(headers)
    # config.get_TemplateCVE(headers)
    # config.get_TemplateCVEItemRegistered(headers)
    # config.get_TemplateCVEItemUnregistered(headers)
    # config.get_TokenUnlimited(headers)
    # config.get_UserAssetGroup(headers)
    # config.get_UserMy(headers)
    # config.get_UserUserGroup(headers)
    # config.get_UserGroup(headers)
    # config.get_UserGroupManage(headers)
    # config.get_UserGroupManageUserRegistered(headers)
    # config.get_UserGroupManageUserUnregistered(headers)