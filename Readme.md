# Resource naming conventions

1. Use nouns not verbs
2. Use plural nouns for collections
3. Use kebab case for path segments
4. Maintain a hierachical structure
5. Use Query parameters for sorting, filtering or pagination
6. Keep URIs Concise and Intuitive
7. Do not use file extensions
8. Never use CRUD function names in URIs
9. Avoid trailing forward slash (/) in URIs
10. Use lowercase letters in URIs

# Benefits of Good API Naming Practices

1. Enhanced Readability and Understanding
2. Improved Consistency
3. Easier Troubleshooting
4. Facilitates Growth and Scalability
5. Better User Experience

# API Versioning Strategies

API versioning is the process of managing and tracking changes to an API. It also involves communicating those changes to the API's consumers.

There are several approaches to API versioning, including:

-   URL versioning: With this approach, the version number is included in the URL of the API endpoint. For instance, consumers who are interested in viewing all of the products in a database would send a request to the https://example-api.com/v1/products endpoint. This is the most popular type of API versioning.
-   Query parameter versioning: This strategy requires users to include the version number as a query parameter in the API request. For instance, they might send a request to https://example-api.com/products?version=v1.
-   Header versioning: This approach allows consumers to pass the version number as a header in the API request, which decouples the API version from the URL structure.
-   Consumer-based versioning: This versioning strategy allows consumers to choose the appropriate version based on their needs. With this approach, the version that exists at the time of the consumer's first call is stored with the consumer's information. Every future call is then executed against this same version—unless the consumer explicitly modifies their configuration.

## References

-   https://restfulapi.net/resource-naming/
-   https://blog.dreamfactory.com/best-practices-for-naming-rest-api-endpoints
-   https://www.postman.com/api-platform/api-versioning/
-   https://www.restapitutorial.com/introduction/restquicktips
