# Shopline SDK for Python

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/badge/pypi-0.1.0-orange.svg)](https://pypi.org/project/shopline-sdk-python/)

一个用于与 Shopline OpenAPI 交互的 Python SDK。基于 [Shopline OpenAPI 文档](https://open-api.docs.shoplineapp.com) 实现。

## 特性

- 🚀 **异步支持**: 基于 `aiohttp` 的异步 HTTP 客户端
- 📝 **类型安全**: 使用 `pydantic` 进行数据验证和类型提示
- 🛡️ **错误处理**: 完善的异常处理机制
- 📚 **完整覆盖**: 支持 Shopline OpenAPI 的所有端点
- 🔧 **易于使用**: 简洁的 API 设计，易于集成

## 安装

```bash
pip install shopline-sdk-python
```

或者使用 uv：

```bash
uv add shopline-sdk-python
```

## 快速开始

### 基本用法

```python
import asyncio
import os
from shopline_sdk.client import ShoplineAPIClient
from shopline_sdk.apis.customers import get_customers

async def main():
    # 创建客户端
    client = ShoplineAPIClient(os.getenv('SHOPLINE_ACCESS_TOKEN'))
    
    # 使用客户端会话
    async with client.new_session() as session:
        # 调用 API
        response = await get_customers.call(session)
        print(f"获取到 {len(response.items)} 个客户")

# 运行异步函数
asyncio.run(main())
```

### 带参数的 API 调用

```python
import asyncio
from shopline_sdk.client import ShoplineAPIClient
from shopline_sdk.apis.customers import get_customers

async def get_recent_customers():
    client = ShoplineAPIClient(os.getenv('SHOPLINE_ACCESS_TOKEN'))
    
    async with client.new_session() as session:
        # 创建查询参数
        params = get_customers.Params(
            page=1,
            per_page=10,
            sort_by='desc',
            include_fields=['metafields']
        )
        
        # 调用 API
        response = await get_customers.call(session, params=params)
        
        for customer in response.items:
            print(f"客户: {customer.email}")

asyncio.run(get_recent_customers())
```

### 创建资源示例

```python
import asyncio
from shopline_sdk.client import ShoplineAPIClient
from shopline_sdk.apis.addon_products import create_addon_product
from shopline_sdk.models.money import Money
from shopline_sdk.models.translatable import Translatable

async def create_addon():
    client = ShoplineAPIClient(os.getenv('SHOPLINE_ACCESS_TOKEN'))
    
    async with client.new_session() as session:
        # 创建加购品请求体
        body = create_addon_product.Body(
            title_translations=Translatable(
                zh_tw="加購商品",
                en="Addon Product"
            ),
            sku="ADDON-001",
            unlimited_quantity=True,
            cost=Money(amount="10.00", currency="USD")
        )
        
        # 调用 API
        addon_product = await create_addon_product.call(session, body=body)
        print(f"创建的加购品 ID: {addon_product.id}")

asyncio.run(create_addon())
```

### 更新资源示例

```python
import asyncio
from shopline_sdk.client import ShoplineAPIClient
from shopline_sdk.apis.customers import update_customer

async def update_customer_info():
    client = ShoplineAPIClient(os.getenv('SHOPLINE_ACCESS_TOKEN'))
    
    async with client.new_session() as session:
        customer_id = "5a55b3c973746f507e120000"
        
        # 创建查询参数（可选字段）
        params = update_customer.Params(
            fields=["id", "email", "name"]  # 只返回指定字段
        )
        
        # 创建请求体（要更新的数据）
        body = update_customer.Body(
            name="张三",
            email="zhangsan@example.com",
            is_accept_marketing=True
        )
        
        # 调用 API
        updated_customer = await update_customer.call(
            session,
            id=customer_id,
            params=params,
            body=body
        )
        print(f"更新的客户: {updated_customer.name} ({updated_customer.email})")

asyncio.run(update_customer_info())
```

## API 覆盖

SDK 支持 Shopline OpenAPI 的所有主要功能模块：

### 客户管理
- 获取客户列表
- 创建、更新、删除客户
- 客户标签管理
- 会员积分管理
- 客户元数据管理

### 产品管理
- 产品 CRUD 操作
- 产品变体管理
- 库存管理
- 加购品管理
- 产品元数据管理

### 订单管理
- 订单查询和管理
- 订单配送管理
- 订单元数据管理

### 营销工具
- 促销活动管理
- 联盟营销
- 优惠券管理
- 会员等级管理

### 其他功能
- 分类管理
- 媒体文件管理
- 主题设置
- 批量操作

## 错误处理

SDK 提供了完善的错误处理机制：

```python
from shopline_sdk.exceptions import ShoplineAPIError

async def handle_errors():
    client = ShoplineAPIClient("invalid_token")
    
    try:
        async with client.new_session() as session:
            response = await get_customers.call(session)
    except ShoplineAPIError as e:
        print(f"API 错误: {e.status_code} - {e.message}")
        print(f"错误代码: {e.code}")
        if e.error:
            print(f"详细错误: {e.error}")
```

## 配置

### 环境变量

建议使用环境变量来管理敏感信息：

```bash
export SHOPLINE_ACCESS_TOKEN="your_access_token_here"
```

### 自定义基础 URL

```python
client = ShoplineAPIClient(
    access_token="your_token",
    base_url="https://custom-api.shopline.io/v1"
)
```

### 自定义请求头

```python
async with client.new_session(headers={"Custom-Header": "value"}) as session:
    # 使用自定义请求头
    response = await get_customers.call(session)
```

## 许可证

本项目采用 GPL-3.0 许可证。详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 链接

- [Shopline OpenAPI 文档](https://open-api.docs.shoplineapp.com)
- [GitHub 仓库](https://github.com/hsojo/shopline-sdk-python)
- [PyPI 包](https://pypi.org/project/shopline-sdk-python/)

## 更新日志

### v0.1.0
- 初始版本发布
- 支持所有 Shopline OpenAPI 端点
- 异步客户端实现
