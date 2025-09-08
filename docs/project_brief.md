# Orbit - Multi-Agent AI System Project Brief

## Project Overview
Orbit is a multi-agent AI framework that automates complex tasks across browsers and applications through a chat interface. Users can request tasks like "book a flight", "compare prices", "fill forms", or "process documents" and the system intelligently routes these to specialized agents that complete the work autonomously.

## Core Architecture

### System Flow
```
User Query → User Agent → Assistant Agent → Specialized Agents → Tools Pool → External Applications
```

### Agent Hierarchy
1. **User Agent**: Primary interface, query processing, response formatting
2. **Assistant Agent**: Workflow coordinator, agent orchestration, error handling
3. **Specialized Agents**: Web Agent, Search Agent, Coding Agent, Document Agent
4. **Tools Pool**: Browser automation, multimodal processing, document handling, code execution
5. **MCP Servers**: Connectors to external apps (YouTube, Spotify, Notion, Gmail, etc.)

## Technology Stack
- **Framework**: Camel-AI for multi-agent coordination
- **Browser Automation**: Playwright for web interactions
- **Backend**: FastAPI + WebSockets for real-time communication
- **Frontend**: Streamlit (MVP) → React/Next.js (production)
- **Document Processing**: LangChain + ChromaDB for RAG
- **Database**: PostgreSQL + Redis for caching
- **Deployment**: Docker containers

## Agent Specifications

### User Agent (`user_agent.py`)
```python
class UserAgent(ChatAgent):
    def __init__(self):
        super().__init__(role_name="User Interface Agent")
        self.conversation_history = []
        self.user_preferences = {}
    
    async def process_query(self, query: str) -> dict:
        intent = self.parse_intent(query)
        entities = self.extract_entities(query)
        return {
            "intent": intent,
            "entities": entities,
            "original_query": query,
            "user_context": self.get_user_context()
        }
```

### Assistant Agent (`assistant_agent.py`)
- **Role**: Workflow coordinator and decision maker
- **Responsibilities**: Agent selection, task decomposition, parallel execution management
- **Features**: Error recovery, progress tracking, result aggregation

### Web Agent (`web_agent.py`)
- **Role**: Browser automation specialist
- **Capabilities**: Form filling, web scraping, price comparison, booking automation
- **Tools**: Playwright browser automation, element detection, anti-bot handling

### Search Agent (`search_agent.py`)
- **Role**: Information retrieval and research
- **Capabilities**: Web search, API data fetching, real-time monitoring
- **Tools**: Search APIs, web scraping, data aggregation

### Coding Agent (`coding_agent.py`)
- **Role**: Code generation and execution
- **Capabilities**: Script writing, automation code, debugging, testing
- **Tools**: Code execution environment, Git integration

### Document Agent (`document_agent.py`)
- **Role**: Document processing and analysis
- **Capabilities**: PDF/Word processing, summarization, Q&A, report generation
- **Tools**: OCR, text extraction, vector embeddings, semantic search

## Key Implementation Components

### Task Classification System
```python
class TaskClassifier:
    def classify_task(self, query: str) -> TaskType:
        # Intent detection logic
        # Entity extraction
        # Agent routing decisions
        pass
```

### Browser Tool (Core Automation)
```python
class BrowserTool:
    async def fill_form(self, url: str, form_data: dict):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            # Form filling automation logic
            await browser.close()
    
    async def scrape_prices(self, product_urls: list):
        # Price comparison automation
        pass
```

### MCP Server Architecture
```python
class MCPServer:
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.connection = None
    
    async def execute_action(self, action: str, params: dict):
        # Execute actions in external applications
        pass
```

## Example Use Cases & Workflows

### 1. Flight Booking
**User**: "Book a flight from Mumbai to Delhi for next Friday under ₹8000"
**Flow**: User Agent → Assistant Agent → Web Agent → Browser Tool → Flight booking sites
**Actions**: Search flights, compare prices, fill booking forms, payment processing

### 2. Price Comparison
**User**: "Compare iPhone 15 prices on Amazon, Flipkart, and Croma"
**Flow**: User Agent → Assistant Agent → Search Agent + Web Agent → Price scraping tools
**Actions**: Parallel price fetching, comparison table generation, deal alerts

### 3. Document Processing
**User**: "Summarize this research paper and answer questions about methodology"
**Flow**: User Agent → Assistant Agent → Document Agent → Document processing tools
**Actions**: PDF parsing, content extraction, summarization, Q&A setup

### 4. Application Control
**User**: "Create a Spotify playlist with my uploaded songs and share it"
**Flow**: User Agent → Assistant Agent → Web Agent → Spotify MCP Server
**Actions**: File processing, playlist creation, sharing configuration

## Development Timeline Options

### 2-Week MVP (Prototype)
- Basic agent coordination with Camel-AI
- Simple browser automation (1-2 sites)
- Document Q&A functionality
- Streamlit chat interface
- 2-3 working demo scenarios

### 4-Week Solid MVP
- Full agent implementation
- Multiple website support
- Basic MCP server integration
- React-based UI
- Comprehensive error handling

### 2-3 Month Production System
- Advanced security features
- Scalable architecture
- Multiple concurrent users
- Extensive application integrations
- Professional UI/UX

## Critical Success Factors

1. **Robust Task Classification**: Accurate intent detection for proper agent routing
2. **Reliable Browser Automation**: Handling dynamic content and anti-bot measures
3. **Error Recovery**: Graceful failure handling and user feedback
4. **User Experience**: Intuitive interface with clear progress indicators
5. **Security**: Proper authentication and data protection

## Technical Challenges

### Browser Automation
- Dynamic content loading
- Anti-bot detection systems
- Cross-site navigation
- Authentication flows

### Agent Coordination
- Task dependency management
- Parallel execution coordination
- Error propagation and recovery
- State synchronization

### External Integrations
- API rate limiting
- Authentication management
- Data format standardization
- Real-time communication

## MVP Implementation Priority

### Week 1 Focus
1. Basic Camel-AI agent setup
2. Simple browser automation tool
3. Intent classification system
4. Agent communication flow

### Week 2 Focus
1. Streamlit chat interface
2. Document processing capability
3. Demo scenario implementation
4. Error handling and polish

## Code Organization
```
orbit/
├── agents/              # All agent implementations
├── tools/               # Shared tool implementations
├── mcp_servers/         # Application connectors
├── core/                # Task classification, coordination
├── ui/                  # User interface components
├── config/              # Configuration and settings
├── tests/               # Unit and integration tests
└── docs/                # Documentation and examples
```

## Environment Requirements
- Python 3.9+
- Node.js 16+ (for frontend)
- Chrome/Chromium browser
- API keys for LLM services
- Development machine with 8GB+ RAM

## Getting Started Commands
```bash
# Setup
pip install camel-ai playwright fastapi streamlit
playwright install chromium

# Run MVP
python main.py
streamlit run ui/chat_interface.py
```

This document contains all essential information for continuing development in new conversations or with team members.