class Queue {
  constructor(maxSize) {
    this.maxSize = maxSize;
    this.queue = [];
    this.front = 0;
    this.rear = 0;
    this.size = 0;
  }

  enqueue(value) {
    if (this.isFull()) {
      console.log('Queue is full.');
      return;
    }
    this.queue[this.rear] = value;
    this.size += 1;
  }

  isFull() {
    return this.size === this.maxSize;
  }
}
