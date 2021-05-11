package algorithm;

import java.util.Arrays;
import java.util.HashMap;

public class MultilevelBrush {
    public static void main(String[] args) {
        String[] enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = {"young", "john", "tod", "emily", "mary"};
        int[] amount = {12, 4, 2, 5, 10};

        System.out.println(Arrays.toString(new MultilevelBrush().solution(enroll, referral, seller, amount)));
    }

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        HashMap<String, Member> members = getMembers(enroll, referral);
        Member member;
        int[] answer = new int[enroll.length];

        for (int i = 0; i < seller.length; i++) {
            member = members.get(seller[i]);
            pay(member, amount[i] * 100);
        }

        for (int i = 0; i < enroll.length; i++) {
            answer[i] = members.get(enroll[i]).getAmount();
        }
        return answer;
    }

    public HashMap<String, Member> getMembers(String[] enroll, String[] referral) {
        HashMap<String, Member> members = new HashMap<>();
        Member member;

        members.put("-", new Member());
        for (int i = 0; i < enroll.length; i++) {
            member = new Member();
            member.setREFERRAL(members.get(referral[i]));
            members.put(enroll[i], member);
        }
        return members;
    }

    public void pay(Member member, int amount) {
        int payment = amount / 10;

        if (member.isCenter() || payment < 1) {
            member.receive(amount);
            return;
        }
        member.receive(amount - payment);
        pay(member.getREFERRAL(), payment);
    }
}

class Member {
    Member REFERRAL;
    int amount = 0;

    public void setREFERRAL(Member REFERRAL) {
        this.REFERRAL = REFERRAL;
    }

    public boolean isCenter() {
        return REFERRAL == null;
    }

    public void receive(int amount) {
        this.amount += amount;
    }

    public Member getREFERRAL() {
        return REFERRAL;
    }

    public int getAmount() {
        return amount;
    }
}