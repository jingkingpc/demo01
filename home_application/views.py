# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.shortcuts import render
from blueking.component.shortcuts import get_client_by_request
from django.http import JsonResponse
def show(request):
# 默认从django settings中获取APP认证信息：应用ID和安全密钥
# 默认从django request中获取用户登录态bk_token
    client = get_client_by_request(request)
    # 参数
    result = client.cc.search_host_lock()
    return JsonResponse(result)
