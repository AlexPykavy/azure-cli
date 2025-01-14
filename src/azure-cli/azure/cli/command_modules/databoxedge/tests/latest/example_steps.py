# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=unused-argument

from .. import try_manual


# EXAMPLE: /Devices/put/DataBoxEdgeDevicePut
@try_manual
def step_device_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device create '
             '--location "eastus" '
             '--sku "Edge" '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_create_min(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device create '
             '--location "eastus" '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Devices/get/DataBoxEdgeDeviceGetByName
@try_manual
def step_device_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device show '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_show_min(test, rg, checks=None):
    return step_device_show(test, rg, checks)


# EXAMPLE: /Devices/get/DataBoxEdgeDeviceGetByResourceGroup
@try_manual
def step_device_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device list '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_list_min(test, rg, checks=None):
    return step_device_list(test, rg, checks)


# EXAMPLE: /Devices/get/DataBoxEdgeDeviceGetBySubscription
@try_manual
def step_device_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device list',
             checks=checks)


@try_manual
def step_device_list2_min(test, rg, checks=None):
    return step_device_list2(test, rg, checks)


# EXAMPLE: /Devices/get/UpdateSummaryGet
@try_manual
def step_device_show_update_summary(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device show-update-summary '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_show_update_summary_min(test, rg, checks=None):
    return step_device_show_update_summary(test, rg, checks)


# EXAMPLE: /Devices/patch/DataBoxEdgeDevicePatch
@try_manual
def step_device_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device update '
             '--name "{myDevice}" '
             '--tags Key1="value1" Key2="value2" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_update_min(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Devices/post/DownloadUpdatesPost
@try_manual
def step_device_download_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device download-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_download_update_min(test, rg, checks=None):
    return step_device_download_update(test, rg, checks)


# EXAMPLE: /Devices/post/InstallUpdatesPost
@try_manual
def step_device_install_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device install-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_install_update_min(test, rg, checks=None):
    return step_device_install_update(test, rg, checks)


# EXAMPLE: /Devices/post/ScanForUpdatesPost
@try_manual
def step_device_scan_for_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device scan-for-update '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_scan_for_update_min(test, rg, checks=None):
    return step_device_scan_for_update(test, rg, checks)


# EXAMPLE: /Alerts/get/AlertGet
@try_manual
def step_alert_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge alert show '
             '--name "159a00c7-8543-4343-9435-263ac87df3bb" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_alert_show_min(test, rg, checks=None):
    return step_alert_show(test, rg, checks)


# EXAMPLE: /Alerts/get/AlertGetAllInDevice
@try_manual
def step_alert_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge alert list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_alert_list_min(test, rg, checks=None):
    return step_alert_list(test, rg, checks)


# EXAMPLE: /BandwidthSchedules/put/BandwidthSchedulePut
@try_manual
def step_bandwidth_schedule_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge bandwidth-schedule create '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--days "Sunday" "Monday" '
             '--rate-in-mbps 100 '
             '--start "0:0:0" '
             '--stop "13:59:0" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_bandwidth_schedule_create_min(test, rg, checks=None):
    return step_bandwidth_schedule_create(test, rg, checks)


# EXAMPLE: /BandwidthSchedules/get/BandwidthScheduleGet
@try_manual
def step_bandwidth_schedule_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge bandwidth-schedule show '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_bandwidth_schedule_show_min(test, rg, checks=None):
    return step_bandwidth_schedule_show(test, rg, checks)


# EXAMPLE: /BandwidthSchedules/get/BandwidthScheduleGetAllInDevice
@try_manual
def step_bandwidth_schedule_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge bandwidth-schedule list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_bandwidth_schedule_list_min(test, rg, checks=None):
    return step_bandwidth_schedule_list(test, rg, checks)


# EXAMPLE: /BandwidthSchedules/delete/BandwidthScheduleDelete
@try_manual
def step_bandwidth_schedule_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge bandwidth-schedule delete -y '
             '--name "bandwidth-1" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_bandwidth_schedule_delete_min(test, rg, checks=None):
    return step_bandwidth_schedule_delete(test, rg, checks)


# EXAMPLE: /Jobs/get/JobsGet
@try_manual
def step_show_job(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge show-job '
             '--name "159a00c7-8543-4343-9435-263ac87df3bb" '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_show_job_min(test, rg, checks=None):
    return step_show_job(test, rg, checks)


# EXAMPLE: /Nodes/get/NodesGetAllInDevice
@try_manual
def step_list_node(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge list-node '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_list_node_min(test, rg, checks=None):
    return step_list_node(test, rg, checks)


# EXAMPLE: /Orders/put/OrderPut
@try_manual
def step_order_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge order create '
             '--device-name "{myDevice}" '
             '--company-name "Microsoft" '
             '--contact-person "John Mcclane" '
             '--email-list "john@microsoft.com" '
             '--phone "(800) 426-9400" '
             '--address-line1 "Microsoft Corporation" '
             '--address-line2 "One Microsoft Way" '
             '--address-line3 "Redmond" '
             '--city "WA" '
             '--country "United States" '
             '--postal-code "98052" '
             '--state "WA" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_order_create_min(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge order create '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Orders/get/OrderGet
@try_manual
def step_order_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge order show '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_order_show_min(test, rg, checks=None):
    return step_order_show(test, rg, checks)


# EXAMPLE: /Orders/get/OrderGetAllInDevice
@try_manual
def step_order_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge order list '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_order_list_min(test, rg, checks=None):
    return step_order_list(test, rg, checks)


# EXAMPLE: /Orders/delete/OrderDelete
@try_manual
def step_order_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge order delete -y '
             '--device-name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_order_delete_min(test, rg, checks=None):
    return step_order_delete(test, rg, checks)


# EXAMPLE: /Devices/delete/DataBoxEdgeDeviceDelete
@try_manual
def step_device_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge device delete -y '
             '--name "{myDevice}" '
             '--resource-group "{rg}"',
             checks=checks)


@try_manual
def step_device_delete_min(test, rg, checks=None):
    return step_device_delete(test, rg, checks)


# EXAMPLE: /Skus/get/ListSkus
@try_manual
def step_list_sku(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az databoxedge list-sku',
             checks=checks)


@try_manual
def step_list_sku_min(test, rg, checks=None):
    return step_list_sku(test, rg, checks)
