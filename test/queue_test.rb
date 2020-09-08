require_relative 'test_helper'


Minitest::Reporters.use! Minitest::Reporters::SpecReporter.new

describe "Test Queue Implementation" do
  it "creates a Queue" do
    q = Queue.new
    expect(q.class).must_equal Queue
  end

  it "adds something to an empty Queue" do
    
    q = Queue.new
    q.enqueue(10)
    expect(q.to_s).must_equal "[10]"
  end

  it "adds multiple somethings to a Queue" do
    
    q = Queue.new
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    expect(q.to_s).must_equal "[10, 20, 30]"
  end

  it "starts the Queue empty" do
    
    q = Queue.new
    q.empty?.must_equal true
  end

  it "a Queue is empty after removing all the elements" do
    
    q = Queue.new
    q.enqueue(5)
    q.enqueue(6)
    expect(q.dequeue).must_equal 5
    expect(q.dequeue).must_equal 6
    expect(q.empty?).must_equal true
  end

  it "can remove something from the Queue" do
    
    q = Queue.new
    q.enqueue(5)
    removed = q.dequeue
    expect(removed).must_equal 5
    expect(q.empty?).must_equal true
  end

  it "removes the right something (LIFO)" do
    
    q = Queue.new
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(7)
    removed = q.dequeue
    expect(removed).must_equal 5
    expect(q.to_s).must_equal "[3, 7]"
  end

  it "properly adjusts the size with enqueueing and dequeueing" do
    
    q = Queue.new
    expect(q.empty?).must_equal true
    q.enqueue(-1)
    q.enqueue(-60)
    expect(q.empty?).must_equal false
    q.dequeue
    q.dequeue
    expect(q.empty?).must_equal true
  end

  it "returns the front element in the Queue" do
    q = Queue.new
    q.enqueue(40)
    q.enqueue(22)
    q.enqueue(3)
    q.dequeue
    expect(q.dequeue).must_equal 22
  end

  it "works with a large Queue" do
    q = Queue.new
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    expect(q.dequeue).must_equal 10
    expect(q.dequeue).must_equal 20
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)
    q.enqueue(110)
    q.enqueue(120)
    q.enqueue(130)
    q.enqueue(140)
    q.enqueue(150)
    q.enqueue(160)
    q.enqueue(170)
    q.enqueue(180)
    q.enqueue(190)
    q.enqueue(200)
    q.enqueue(210)
    q.dequeue

    expect(q.to_s).must_equal('[40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]')
  end
end
