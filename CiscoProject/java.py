---
- hosts: all
  tasks:
    - name: Task 1 Update APT package manager repositories cache
      become: true
      apt:
        update_cache: yes
    - name: Task -2 Install Java using Ansible
      become: yes
      apt:
        name: "{{ packages }}"