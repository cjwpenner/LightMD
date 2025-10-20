# API Documentation Template
Generate comprehensive API documentation from code or specifications.

## Metadata
---
version: 1.0
author: [Your Name]
created: YYYY-MM-DD
api_type: [REST | GraphQL | gRPC | WebSocket]
target_model: [OpenAI GPT-4o, Claude Sonnet, etc.]
---

## Purpose
[Document API endpoints for developers to integrate with the service]

## API Overview
- **Base URL**: `{{BASE_URL}}`
- **Version**: `{{API_VERSION}}`
- **Authentication**: [Bearer Token | API Key | OAuth 2.0 | None]
- **Rate Limits**: [e.g., 1000 requests/hour]
- **Content Type**: application/json

## Endpoints to Document
[Paste code, OpenAPI spec, or list endpoints here]

## Documentation Requirements
For each endpoint, provide:

### Endpoint Name
**Description**: [What this endpoint does]

**HTTP Method**: `GET | POST | PUT | DELETE | PATCH`

**URL**: `/api/{{VERSION}}/{{RESOURCE}}`

**Authentication Required**: Yes/No

**Request Headers**
```
Authorization: Bearer {{TOKEN}}
Content-Type: application/json
```

**Path Parameters**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| id | integer | Yes | User ID |

**Query Parameters**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 10 | Items per page |

**Request Body**
```json
{
  "field_name": "value",
  "required_field": "example"
}
```

**Response**
- **Status Code**: 200 OK
- **Response Body**:
```json
{
  "data": {},
  "message": "Success",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

**Error Responses**
| Status Code | Description | Example |
|-------------|-------------|---------|
| 400 | Bad Request | Missing required field |
| 401 | Unauthorized | Invalid token |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal error |

**Example Request**
```bash
curl -X POST {{BASE_URL}}/api/v1/users \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

**Example Response**
```json
{
  "id": 123,
  "name": "John Doe",
  "created_at": "2024-01-01T12:00:00Z"
}
```

## Output Format
- Markdown with clear section headers
- Code blocks with syntax highlighting
- Tables for parameters
- Real-world examples
- Links to related endpoints

## Additional Sections
- [ ] Authentication flow
- [ ] Webhook documentation
- [ ] SDK examples (Python, JavaScript, etc.)
- [ ] Changelog
- [ ] Troubleshooting guide
