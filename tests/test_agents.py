"""\nComprehensive Testing Suite for AI Executive Agent
Tests for OpenManus, Comet ML, and core agent functionality
"""

import unittest
import asyncio
from datetime import datetime
import json


class TestOpenManusAgent(unittest.TestCase):
    """Test OpenManus Agent Integration"""
    
    def setUp(self):
        """Initialize test fixtures"""
        print("\n" + "="*60)
        print("Setting up OpenManus Agent Tests...")
        print("="*60)
        self.test_results = []
    
    def test_agent_initialization(self):
        """Test 1: Agent Initialization"""
        print("\n✓ TEST 1: Agent Initialization")
        try:
            from integrations.openmanus import OpenManusAgent
            agent = OpenManusAgent(api_key="test_key")
            
            # Verify attributes
            self.assertIsNotNone(agent)
            self.assertEqual(agent.model, "gpt-4o-mini")
            self.assertEqual(len(agent.capabilities), 6)
            self.assertIn("autonomous_task_execution", agent.capabilities)
            self.assertIn("web_browsing", agent.capabilities)
            self.assertIn("code_generation", agent.capabilities)
            
            print("  ✓ Agent initialized successfully")
            print(f"  ✓ Model: {agent.model}")
            print(f"  ✓ Capabilities: {len(agent.capabilities)}")
            print(f"  ✓ Capabilities list: {', '.join(agent.capabilities)}")
            
            self.test_results.append({
                "test": "Agent Initialization",
                "status": "PASS",
                "details": "Agent created with all expected attributes"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Agent Initialization",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Agent initialization failed: {str(e)}")
    
    def test_task_preparation(self):
        """Test 2: Task Preparation"""
        print("\n✓ TEST 2: Task Preparation")
        try:
            from integrations.openmanus import OpenManusAgent
            agent = OpenManusAgent()
            
            task_desc = "Test task for preparation"
            prepared = agent._prepare_task(task_desc)
            
            self.assertIn("description", prepared)
            self.assertIn("capabilities_available", prepared)
            self.assertIn("model", prepared)
            self.assertIn("timestamp", prepared)
            self.assertEqual(prepared["description"], task_desc)
            self.assertEqual(prepared["model"], "gpt-4o-mini")
            
            print("  ✓ Task prepared successfully")
            print(f"  ✓ Prepared task keys: {', '.join(prepared.keys())}")
            print(f"  ✓ Capabilities in prepared task: {len(prepared['capabilities_available'])}")
            
            self.test_results.append({
                "test": "Task Preparation",
                "status": "PASS",
                "details": "Task prepared with all required fields"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Task Preparation",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Task preparation failed: {str(e)}")
    
    def test_task_id_generation(self):
        """Test 3: Task ID Generation"""
        print("\n✓ TEST 3: Task ID Generation")
        try:
            from integrations.openmanus import OpenManusAgent
            agent = OpenManusAgent()
            
            task_ids = [agent._generate_task_id() for _ in range(5)]
            
            # Verify uniqueness
            self.assertEqual(len(task_ids), len(set(task_ids)))
            
            # Verify format
            for task_id in task_ids:
                self.assertTrue(task_id.startswith("om-"))
                print(f"  ✓ Generated Task ID: {task_id}")
            
            self.test_results.append({
                "test": "Task ID Generation",
                "status": "PASS",
                "details": "5 unique task IDs generated successfully"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Task ID Generation",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Task ID generation failed: {str(e)}")
    
    def test_async_task_execution(self):
        """Test 4: Async Task Execution"""
        print("\n✓ TEST 4: Async Task Execution")
        try:
            from integrations.openmanus import OpenManusAgent
            agent = OpenManusAgent()
            
            async def run_test():
                result = await agent.execute_task(
                    task_description="Test task",
                    use_browser=True,
                    timeout=10
                )
                return result
            
            # Run async test
            result = asyncio.run(run_test())
            
            self.assertIsNotNone(result)
            self.assertIn("task_id", result)
            self.assertIn("status", result)
            self.assertEqual(result["status"], "completed")
            
            print(f"  ✓ Task executed: {result['task_id']}")
            print(f"  ✓ Status: {result['status']}")
            print(f"  ✓ Result keys: {', '.join(result.keys())}")
            
            self.test_results.append({
                "test": "Async Task Execution",
                "status": "PASS",
                "details": f"Task {result['task_id']} executed successfully"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Async Task Execution",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Async task execution failed: {str(e)}")
    
    def test_task_history(self):
        """Test 5: Task History Tracking"""
        print("\n✓ TEST 5: Task History Tracking")
        try:
            from integrations.openmanus import OpenManusAgent
            agent = OpenManusAgent()
            
            # Manually add test entries
            for i in range(3):
                agent.task_history.append({
                    "task_id": f"om-test-{i}",
                    "status": "completed",
                    "timestamp": datetime.now().isoformat()
                })
            
            history = agent.get_task_history(limit=2)
            
            self.assertEqual(len(history), 2)
            print(f"  ✓ History retrieved: {len(history)} tasks")
            
            for task in history:
                print(f"  ✓ Task: {task['task_id']} - {task['status']}")
            
            self.test_results.append({
                "test": "Task History Tracking",
                "status": "PASS",
                "details": f"Retrieved {len(history)} tasks from history"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Task History Tracking",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Task history tracking failed: {str(e)}")
    
    def test_workflow_manager(self):
        """Test 6: Workflow Manager"""
        print("\n✓ TEST 6: Workflow Manager")
        try:
            from integrations.openmanus import OpenManusAgent, OpenManusWorkflow
            agent = OpenManusAgent()
            workflow = OpenManusWorkflow(agent)
            
            self.assertIsNotNone(workflow)
            self.assertEqual(workflow.agent, agent)
            self.assertEqual(len(workflow.workflows), 0)
            
            print("  ✓ Workflow manager initialized")
            print("  ✓ Workflows dictionary: empty")
            
            self.test_results.append({
                "test": "Workflow Manager",
                "status": "PASS",
                "details": "Workflow manager created successfully"
            })
        except Exception as e:
            print(f"  ✗ Test failed: {str(e)}")
            self.test_results.append({
                "test": "Workflow Manager",
                "status": "FAIL",
                "details": str(e)
            })
            self.fail(f"Workflow manager test failed: {str(e)}")
    
    def tearDown(self):
        """Generate test report"""
        print("\n" + "="*60)
        print("TEST SUMMARY REPORT")
        print("="*60)
        
        passed = sum(1 for r in self.test_results if r["status"] == "PASS")
        failed = sum(1 for r in self.test_results if r["status"] == "FAIL")
        total = len(self.test_results)
        
        for i, result in enumerate(self.test_results, 1):
            status_symbol = "✓" if result["status"] == "PASS" else "✗"
            print(f"\n{i}. {status_symbol} {result['test']}: {result['status']}")
            print(f"   Details: {result['details']}")
        
        print("\n" + "="*60)
        print(f"RESULTS: {passed}/{total} PASSED, {failed}/{total} FAILED")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        print("="*60 + "\n")
        
        # Save report to file
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "success_rate": f"{(passed/total)*100:.1f}%",
            "tests": self.test_results
        }
        
        with open("test_report.json", "w") as f:
            json.dump(report, f, indent=2)
        
        print("✓ Test report saved to test_report.json\n")


if __name__ == "__main__":
    print("\n" + "#"*60)
    print("# AI Executive Agent - Test Suite")
    print("# Testing OpenManus Integration")
    print("#"*60)
    
    # Run tests
    unittest.main(verbosity=2)
